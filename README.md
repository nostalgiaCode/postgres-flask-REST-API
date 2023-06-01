# postgres-flask-REST-API

Использовались postgres, sqlalchemy, flask, docker.

Примеры запросов:
  1. POST запрос на получение id и token
curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"test\"}" http://localhost:80
>
{
"id": "lYFueLWZ",
"token": "a3d2cc29-9756-4a94-a302-33b6109be07b"
}
>
  3. POST запрос на загрузку аудиофайла в формате .wav
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/User/audio.wav" -F "json={\"id_user\": \"lYFueLWZ\", \"token\": \"a3d2cc29-9756-4a94-a302-33b6109be07b\"};type=application/json" http://localhost:80/upload
>
"http://localhost/record?id=YUzj0TDc&user=lYFueLWZ"
>
  5. GET запрос на скачивание аудиофайла в формате .mp3
curl "http://localhost/record?id=djbCcW6h&user=lYFueLWZ" --output mymp3.mp3
>
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 13600  100 13600    0     0  13600      0  0:00:01 --:--:--  0:00:01  428k
>
