import json
import os
from os.path import exists

from flask import request
from flask_restful import Resource

from config import UPLOAD_FOLDER
from db import db
from models.user import UserModel
from utils.func import allowed_file, convert_sound, get_random_name

class UploadFile(Resource):
    def post(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            data = json.loads(request.form.to_dict()['json'])
            try:
                user=UserModel.get_user(data['id_user'], data['token'])
                record_name = get_random_name()
                file.save(os.path.join(UPLOAD_FOLDER, record_name + ".wav"))
                if(user.record_id != None):
                    if(exists(UPLOAD_FOLDER + user.record_id + ".mp3") == True):
                        os.remove(UPLOAD_FOLDER + user.record_id + ".mp3")
                    user.record_id = None
                    db.session.commit()
                user.record_id = record_name
                db.session.commit()

                convert_sound(record_name)

                return f"http://{request.host}/record?id={record_name}&user={data['id_user']}"
            except:
                return {'message': 'Unauthorized'}, 401
        else:
            return {'message': 'Unsupported Media Type'}, 415