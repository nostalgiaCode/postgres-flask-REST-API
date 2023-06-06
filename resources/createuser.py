from flask import request
from flask_restful import Resource

from db import db
from models.user import UserModel


class UserCreator(Resource):
    def post(self):    
        try:
            request_data = request.get_json()
            name = request_data['username']
        except:
            return {'message': 'invalid_json'}, 400
        
        if len(name) < 6 or len(name) > 15:
            return {'message' : 'username length betweer 6 and 15 characters'}, 400

        user=UserModel(username=name)
        if(UserModel.get_user(username=name) == None):
            db.session.add(user)
            db.session.commit()
            data = {
                "id" : user.id,
                "token" : str(user.uuid),
            }
            return data, 201
        else:
            user=UserModel.get_user(username=name)
            data = {
                "message" : "user already exists",
                "id" : user.id,
                "token" : str(user.uuid),
            }
            return data, 201