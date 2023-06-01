FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip --user
RUN pip install -r requirements.txt
RUN apk add ffmpeg
EXPOSE 5000
CMD python ./app.py
