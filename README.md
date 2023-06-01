# postgres-flask-REST-API

Использовались postgres, sqlalchemy, flask, docker.

##Установка
Для установки сервиса на Windows 10 убедитесь, что у вас установлен и запущен Docker Desktop (устанавливается только на Windows 10 Enterprise, Pro, or Education издания), скачайте docker-compose.yml файл и перенесите его в отдельную папку. В терминале перейдите в папку, содержащую docker-compose.yml файл и введите команду docker compose up. Docker сам скачает все необходимые образы с Docker Hub'а и запустит сервис.
Инструкции по сборке содержатся в файлах docker-compose.yml и Dockerfile. URI для подключения к postgres БД находится в файле config.py.

##Примеры запросов:
  1. POST запрос на получение id и token
```
curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"test\"}" http://localhost:80
```
```
{
"id": "lYFueLWZ",
"token": "a3d2cc29-9756-4a94-a302-33b6109be07b"
}
```
  2. POST запрос на загрузку аудиофайла в формате .wav
```
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/User/audio.wav" -F "json={\"id_user\": \"lYFueLWZ\", \"token\": \"a3d2cc29-9756-4a94-a302-33b6109be07b\"};type=application/json" http://localhost:80/upload
```
```
"http://localhost/record?id=YUzj0TDc&user=lYFueLWZ"
```
  3. GET запрос на скачивание аудиофайла в формате .mp3
```
curl "http://localhost/record?id=djbCcW6h&user=lYFueLWZ" --output mymp3.mp3
```
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 13600  100 13600    0     0  13600      0  0:00:01 --:--:--  0:00:01  428k
```
