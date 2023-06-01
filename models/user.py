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

    def get_user(id=None, uuid=None, record_id=None, username=None):
        if id is not None and uuid is not None and record_id is None and username is None:
            return UserModel.query.filter_by(id=id, uuid=uuid).first()
        elif id is not None and record_id is not None and uuid is None and username is None:
            return UserModel.query.filter_by(id=id, record_id=record_id).first()
        elif username is not None and id is None and record_id is None and uuid is None:
            return UserModel.query.filter_by(username=username).first()
    