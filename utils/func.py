import os
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from pydub import AudioSegment
import base64

def convert_sound(name):
    sound = AudioSegment.from_file(UPLOAD_FOLDER + name + ".wav")
    sound.export(UPLOAD_FOLDER + name + ".mp3", format = "mp3")
    os.remove(UPLOAD_FOLDER + name + ".wav")

def get_random_name():
    return base64.urlsafe_b64encode(os.urandom(6)).decode('ascii')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS