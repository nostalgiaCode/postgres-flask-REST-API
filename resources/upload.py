import base64
import json
import os
from os.path import exists

from flask import request
from flask_restful import Resource
from pydub import AudioSegment

from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from db import db
from models.user import UserModel

class Uploader(Resource):
    def post(self):
        file = request.files['file']
        if file and Uploader.allowed_file(file.filename):
            try:
                data = json.loads(request.form.to_dict()['json'])
                user_id = data['id_user']
                user_uuid = data['token']
            except:
                return {'message': 'Invalid json'}, 400
            try:
                user=UserModel.get_user(id=user_id, uuid=user_uuid)
                print(user.id, user.record_id)
                record_name = Uploader.get_random_name()
                print(record_name)
                Uploader.convert_audio(record_name, user, file, db)
                print("AUDIO CONVERTED")
                return f"http://{request.host}/record?id={record_name}&user={user_id}", 200
            except:
                return {'message': 'Unauthorized'}, 401
        else:
            return {'message': 'Unsupported Media Type'}, 415
        
    def convert_audio(record_name, user, file, db):
        file.save(os.path.join(UPLOAD_FOLDER, record_name + ".wav"))
        if(user.record_id != None):
            if(exists(UPLOAD_FOLDER + user.record_id + ".mp3") == True):
                os.remove(UPLOAD_FOLDER + user.record_id + ".mp3")
            user.record_id = None
            db.session.commit()
        user.record_id = record_name
        db.session.commit()
        Uploader.convert_sound(record_name)

    def convert_sound(name):
        sound = AudioSegment.from_file(UPLOAD_FOLDER + name + ".wav")
        sound.export(UPLOAD_FOLDER + name + ".mp3", format = "mp3")
        os.remove(UPLOAD_FOLDER + name + ".wav")

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    def get_random_name():
        return base64.urlsafe_b64encode(os.urandom(6)).decode('ascii')
