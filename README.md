# Forest Fire Segmentation

## Description

Fire segmentation in your video forest fire with GUI application based. \
You can use this code for other segmentation, but you must have a color space method, value upper bound, a value lower bound and your video for segmentation.

## Recommended Value

1. **LAB**
    1. Lower = [82, 0, 159] \
       Upper = [255, 255, 255]
    2. Lower = [157, 0, 148] \
       Upper = [255, 255, 255]
    3. Lower = [112, 0, 160] \
       Upper = [255, 255, 255]
    4. Lower = [114, 0, 168] \
       Upper = [255, 182, 255]
    5. Lower = [203, 0, 112] \
       Upper = [255, 255, 255]
    6. Lower = [117, 0, 156] \
       Upper = [255, 255, 255]
    7. Lower = [134, 0, 149] \
       Upper = [255, 240, 255]
2. **HSV**
    1. Lower = [0, 0, 148] \
       Upper = [179, 255, 255]
    2. Lower = [6, 0, 216] \
       Upper = [98, 255, 255]
    3. Lower = [0, 143, 132] \
       Upper = [179, 255, 255]
    4. Lower = [0, 0, 210] \
       Upper = [50, 255, 255]
    5. Lower = [0, 0, 198] \
       Upper = [179, 255, 255]
    6. Lower = [2, 48, 165] \
       Upper = [151, 255, 255]
    7. Lower = [1, 29, 181] \
       Upper = [137, 255, 255]
3. **YCrCb**
    1. Lower = [103, 0, 0] \
       Upper = [255, 255, 255]
    2. Lower = [152, 0, 0] \
       Upper = [255, 255, 112]
    3. Lower = [98, 0, 0] \
       Upper = [255, 255, 86]
    4. Lower = [121, 103, 0] \
       Upper = [255, 255, 255]
    5. Lower = [130, 0, 70] \
       Upper = [255, 255, 255]
    6. Lower = [119, 0, 0] \
       Upper = [255, 255, 151]
    7. Lower = [121, 21, 14] \
       Upper = [255, 255, 193]

## Installation

### Installation Python

```bash
# Python version 3.8 or more
$ pip install -r requirements.txt

# (Optional) Download example video
$ python download_video.py
```

### Installation Docker

```bash
# Newest docker version
$ docker build -t hafidh561/forest-fire-segmentation:1.0 .
```

## Usage

### Usage Python

```bash
$ python app.py -h
usage: app.py [-h] [-l LOWER [LOWER ...]] [-u UPPER [UPPER ...]] [-m METHOD] [-haf HIGH_AREA_FIRE] [-maf MEDIUM_AREA_FIRE] [-laf LOW_AREA_FIRE]
              [-v VIDEO] [-ffv FOREST_FIRE_VIDEO]

optional arguments:
  -h, --help            show this help message and exit
  -l LOWER [LOWER ...], --lower LOWER [LOWER ...]
                        Input your lower bound value
  -u UPPER [UPPER ...], --upper UPPER [UPPER ...]
                        Input your upper bound value
  -m METHOD, --method METHOD
                        Input your color space method
  -haf HIGH_AREA_FIRE, --high-area-fire HIGH_AREA_FIRE
                        Input your minimal value to detect high area fire
  -maf MEDIUM_AREA_FIRE, --medium-area-fire MEDIUM_AREA_FIRE
                        Input your minimal value to detect medium area fire
  -laf LOW_AREA_FIRE, --low-area-fire LOW_AREA_FIRE
                        Input your minimal value to detect low area fire
  -v VIDEO, --video VIDEO
                        Input your video source
  -ffv FOREST_FIRE_VIDEO, --forest-fire-video FOREST_FIRE_VIDEO
                        Forest fire video True or False

# Example arguments input
$ python app.py -l 121 21 14 -u 255 255 193 -m ycrcb -haf 7000 -maf 3500 -laf 100 -v ./src/video2.mp4 -ffv true
```

### Usage Docker

#### Prerequisite for Windows

1. Download and install [VcXsrv](https://sourceforge.net/projects/vcxsrv/)
2. Run VcXsrv before run this docker app

#### Prerequisite for Linux

```bash
# Exposo your xhost
$ xhost +local:docker

# When you finish, you can return the access control by using the following
$ # xhost -local:docker

# Add environment variables
$ XSOCK=/tmp/.X11-unix
$ XAUTH=/tmp/.docker.xauth

# Create the authentication files
$ touch /tmp/.docker.xauth

# Create permission
$ xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -
```

```bash
$ docker run --rm -e hafidh561/forest-fire-segmentation:1.0 -h
usage: app.py [-h] [-l LOWER [LOWER ...]] [-u UPPER [UPPER ...]] [-m METHOD]
              [-haf HIGH_AREA_FIRE] [-maf MEDIUM_AREA_FIRE]
              [-laf LOW_AREA_FIRE] [-v VIDEO] [-ffv FOREST_FIRE_VIDEO]

optional arguments:
  -h, --help            show this help message and exit
  -l LOWER [LOWER ...], --lower LOWER [LOWER ...]
                        Input your lower bound value
  -u UPPER [UPPER ...], --upper UPPER [UPPER ...]
                        Input your upper bound value
  -m METHOD, --method METHOD
                        Input your color space method
  -haf HIGH_AREA_FIRE, --high-area-fire HIGH_AREA_FIRE
                        Input your minimal value to detect high area fire
  -maf MEDIUM_AREA_FIRE, --medium-area-fire MEDIUM_AREA_FIRE
                        Input your minimal value to detect medium area fire
  -laf LOW_AREA_FIRE, --low-area-fire LOW_AREA_FIRE
                        Input your minimal value to detect low area fire
  -v VIDEO, --video VIDEO
                        Input your video source
  -ffv FOREST_FIRE_VIDEO, --forest-fire-video FOREST_FIRE_VIDEO
                        Forest fire video True or False

# Example arguments input
$ docker run --rm -e DISPLAY=192.168.0.2:0 hafidh561/forest-fire-segmentation:1.0 -l 121 21 14 -u 255 255 193 -m hsv -haf 7000 -maf 3500 -laf 100 -v ./src/video2.mp4 -ffv true

# For Operating System Windows
$ docker run --rm -e DISPLAY=<your local ip address>:0 hafidh561/forest-fire-segmentation:1.0

# For Operating System Linux
$ docker run --rm -e DISPLAY=$DISPLAY hafidh561/forest-fire-segmentation:1.0
```

## Screenshots

![video1.mp4](./screenshots/ss1.png "video1.mp4")

![video2.mp4](./screenshots/ss2.png "video2.mp4")

![video3.mp4](./screenshots/ss3.png "video3.mp4")

![video4.mp4](./screenshots/ss4.png "video4.mp4")

## License

[MIT LICENSE](./LICENSE)

## Changelog

-   **1.0** Forest Fire Segmentation

© Developed by [hafidh561](https://github.com/hafidh561) - Internship at Nodeflux
