import base64
import os
import uuid

from db import db


class UserModel(db.Model):
    id = db.Column(db.String(8), default=None, primary_key=True)
    uuid = db.Column(db.String(200), default=None)
    username = db.Column(db.String(200))
    record_id = db.Column(db.String(200), default=None)

    def __init__(self, username):
        self.id = base64.urlsafe_b64encode(os.urandom(6)).decode('ascii')
        self.uuid = str(uuid.uuid4())
        self.username = username

    def get_user(given_id, given_uuid):
        return UserModel.query.filter_by(id=given_id, uuid=given_uuid).first()
    