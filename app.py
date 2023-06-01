import os

from flask import Flask
from flask_restful import Api

from config import UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@pgsql:5432/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

api = Api(app)

from resources.download import RecordFile
from resources.newuser import User
from resources.upload import UploadFile

api.add_resource(User, '/')
api.add_resource(UploadFile, '/upload')
api.add_resource(RecordFile, '/record', endpoint='record')

if __name__ == "__main__":
    with app.app_context():
        from db import db
        db.init_app(app)
        db.create_all()
        app.run(debug=True, host='0.0.0.0')

        