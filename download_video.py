import gdown
import os

if "test_video" not in os.listdir():
    os.makedirs("test_video")

# Video Example
url = "https://drive.google.com/u/4/uc?id=1E6ZozTpcALJdzMOCQDSErRktN9BF1znE&export=download"
gdown.download(url, "./test_video/video1.mp4")

# Video Example
url = "https://drive.google.com/u/4/uc?id=1U0tvUBod2jJw8dcm-4uE49DGsKPMg4so&export=download"
gdown.download(url, "./test_video/video2.mp4")

# Video Example
url = "https://drive.google.com/u/4/uc?id=1UDbv-cVPloX7y6vG2aL4IFTYRe1BCmoP&export=download"
gdown.download(url, "./test_video/video3.mp4")

# Video Example
url = "https://drive.google.com/u/4/uc?id=15sfgAT9gD4e-6-xhwSrrI2kMWXI2kAtL&export=download"
gdown.download(url, "./test_video/video4.mp4")
