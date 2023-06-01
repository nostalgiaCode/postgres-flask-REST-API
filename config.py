import os

folder = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = folder + "/uploads/"
ALLOWED_EXTENSIONS = {"wav"}

postgresqldocker = "postgresql://postgres:1234@pgsql:5432/"
postgresqllocal = "postgresql://postgres:1234@localhost:5432/"