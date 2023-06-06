import os

from flask import Flask
from flask_restful import Api

from config import UPLOAD_FOLDER, postgresql

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresql
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

api = Api(app)

from resources.download import Downloader
from resources.createuser import UserCreator
from resources.upload import Uploader

api.add_resource(UserCreator, '/')
api.add_resource(Uploader, '/upload')
api.add_resource(Downloader, '/record', endpoint='record')

if __name__ == "__main__":
    with app.app_context():
        from db import db
        db.init_app(app)
        db.create_all()
        app.run(host='0.0.0.0')

        