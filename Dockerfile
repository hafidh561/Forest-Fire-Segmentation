# Install Images
FROM python:3.8.12-slim

# Set working directory
WORKDIR /home/app

# Install packages
RUN apt-get update -y && apt-get upgrade -y && \
apt-get install ffmpeg libsm6 libxext6 -y && \
apt-get install tk -y

# Copy all files into working directory
COPY app.py download_video.py requirements.txt /home/app/
COPY ForestFireSegmentation/ /home/app/ForestFireSegmentation/
COPY test_video/ /home/app/test_video/

# Instal python libraries
RUN pip install -r requirements.txt

# Run script
ENTRYPOINT ["python", "app.py"]