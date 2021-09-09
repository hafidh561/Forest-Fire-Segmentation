FROM python:3.8.12-slim

RUN mkdir /home/app /home/app/src /home/app/ForestFireSegmentation

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install tk -y

COPY app.py /home/app
COPY download_video.py /home/app
COPY requirements.txt /home/app
COPY ForestFireSegmentation /home/app/ForestFireSegmentation

WORKDIR /home/app

RUN pip install -r requirements.txt

RUN python download_video.py

ENTRYPOINT ["python", "app.py"]