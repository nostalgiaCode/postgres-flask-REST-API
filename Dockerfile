FROM python:3.9-alpine
WORKDIR /app
COPY . /app
#RUN wget http://launchpadlibrarian.net/339874908/libav-tools_3.3.4-2_all.deb
#RUN apk add ./libav-tools_3.3.4-2_all.deb
RUN pip install --upgrade pip --user
RUN pip install -r requirements.txt
#RUN ffdl install --add-path
RUN apk add ffmpeg
EXPOSE 5000
CMD python ./app.py
