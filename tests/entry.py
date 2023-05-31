import requests

url = 'http://localhost:5000/'
myobj = {'username': 'test'}

x = requests.post(url, json = myobj)

print(x.text)