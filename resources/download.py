from flask import request, send_from_directory, jsonify
from flask_restful import Resource

from config import UPLOAD_FOLDER
from models.user import UserModel

class Downloader(Resource):
    def get(self): 
        try:
            id_record = request.args.get('id')
            print(id_record)
            user = request.args.get('user')
            print(user)
        except:
            return {'message' : 'Invalid input'}, 400
        if(UserModel.get_user(id=user, record_id=id_record)):
            try:
                return send_from_directory(directory=UPLOAD_FOLDER,
                               path=id_record+".mp3", as_attachment=True)
            except:
                {'message' : 'Record not found'}, 404
        else:
            return {'message' : 'Wrong user_id or record_id'}, 400