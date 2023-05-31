import base64
import json
import os
import uuid
from os.path import exists

from flask import Flask, jsonify, request, send_from_directory
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from pydub import AudioSegment

folder = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = folder + "/uploads/"
ALLOWED_EXTENSIONS = {'wav'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@pgsql:5432/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class users(db.Model):
    id = db.Column(db.String(8), default=None, primary_key=True)
    uuid = db.Column(db.String(200), default=None)
    username = db.Column(db.String(200))
    record_id = db.Column(db.String(200), default=None)

    def __init__(self, username):
        if username == "admin":
            self.id = "0000"
            self.uuid = "0000"
        if self.id is None:
            self.id = base64.urlsafe_b64encode(os.urandom(6)).decode('ascii')
        if self.uuid is None:
            self.uuid = str(uuid.uuid4())
        self.username = username

class RecordAPI(Resource):
    def get(self): 
        id_record = request.args.get('id')
        user = request.args.get('user')
        if(users.query.filter_by(id=user, record_id=id_record).first()!=None):
            return send_from_directory(directory=app.config['UPLOAD_FOLDER'],
                               path=id_record+".mp3", as_attachment=True)
        else:
            return "Smth bad happened!"
api.add_resource(RecordAPI, '/record', endpoint='record')


admin_user=users(username="admin")

@app.route('/', methods=['POST'])
def default():
    if request.method=='POST':    
        request_data = request.get_json()
        name = request_data['username']

        user=users(username=name)
        if(users.query.filter_by(username=name).first() == None):
            db.session.add(user)
            db.session.commit()
        else:
            user=users.query.filter_by(username=name).first()
        data = {
            "id" : user.id,
            "token" : user.uuid,
        }
        return jsonify(data)

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            data = json.loads(request.form.to_dict()['json'])
            id_user = data['id_user']
            token = data['token']

            if(users.query.filter_by(id=id_user, uuid=token).first() != None):
                name = base64.urlsafe_b64encode(os.urandom(6)).decode('ascii')
                file = request.files['file']
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], name + ".wav"))
                
                user=users.query.filter_by(id=id_user, uuid=token).first()
                if(user.record_id != None):
                    if(exists(app.config['UPLOAD_FOLDER'] + user.record_id + ".mp3") == True):
                        os.remove(app.config['UPLOAD_FOLDER'] + user.record_id + ".mp3")
                    user.record_id = None
                    db.session.commit()
                user.record_id = name
                db.session.commit()

                sound = AudioSegment.from_file(UPLOAD_FOLDER + name + ".wav")
                sound.export(UPLOAD_FOLDER + name + ".mp3", format = "mp3")
                os.remove(app.config['UPLOAD_FOLDER'] + name + ".wav")

                return_string = "http://{0}/".format(request.host) + "record?id="+name+"&user="+id_user
                return return_string
            else:
                return "Not auth!"
        else:
            return "Wrong file format!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, host='0.0.0.0')

        