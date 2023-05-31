from flask import request, send_from_directory
from flask_restful import Resource

from config import UPLOAD_FOLDER
from models.user import UserModel

class RecordFile(Resource):
    def get(self): 
        id_record = request.args.get('id')
        user = request.args.get('user')
        if(UserModel.get_user(id=user, record_id=id_record)!=None):
            try:
                return send_from_directory(directory=UPLOAD_FOLDER,
                               path=id_record+".mp3", as_attachment=True)
            except:
                {'message' : 'Record not found'}, 404
        else:
            return {'message' : 'Wrong user_id or record_id'}, 401