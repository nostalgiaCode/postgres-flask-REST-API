from flask import jsonify, request
from flask_restful import Resource

from db import db
from models.user import UserModel


class User(Resource):
    def post(self):    
        request_data = request.get_json()
        name = request_data['username']

        user=UserModel(username=name)
        if(UserModel.get_user(name) == None):
            db.session.add(user)
            db.session.commit()
        else:
            user=UserModel.get_user(name)
        data = {
            "id" : user.id,
            "token" : user.uuid,
        }
        return jsonify(data)