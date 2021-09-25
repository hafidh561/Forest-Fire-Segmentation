# Install Images
FROM python:3.8.12-slim

# Set working directory
WORKDIR /home/app

# Create directory for video
RUN mkdir /home/app/test_video /home/app/ForestFireSegmentation

# Install packages
RUN apt-get update -y && apt-get upgrade -y && \
apt-get install ffmpeg libsm6 libxext6 -y && \
apt-get install tk -y

# Copy all files into working directory
COPY app.py download_video.py requirements.txt /home/app/
COPY ForestFireSegmentation /home/app/ForestFireSegmentation

# Instal python libraries
RUN pip install -r requirements.txt

# (OPTIONAL) Download example video
# Make sure put your video in directory ./test_video/
RUN python download_video.py

# Run script
ENTRYPOINT ["python", "app.py"]