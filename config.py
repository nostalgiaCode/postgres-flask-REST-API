import os

folder = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = folder + "/uploads/"
ALLOWED_EXTENSIONS = {'wav'}