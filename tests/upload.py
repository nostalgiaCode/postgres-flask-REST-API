import requests
import json
import os

url = 'http://localhost:5000/upload'
payload = {"id_user": "Aj0Vej3X",
    "token": "09f8f61d-bcca-41ae-abeb-54f34f00ff0e"}
file = "C:/Users/Жан/projects/testtask/tests/battle.wav"
files = {
        'json': (None, json.dumps(payload), 'application/json'),
        'file': (os.path.basename(file), open(file, 'rb'), 'application/octet-stream')
    }
res = requests.post(url, files=files)
print(res.text)