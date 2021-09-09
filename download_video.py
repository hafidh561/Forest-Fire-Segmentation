import gdown
import shutil
import os

if "src" not in os.listdir():
    os.makedirs("src")

url = "https://drive.google.com/u/4/uc?id=1E6ZozTpcALJdzMOCQDSErRktN9BF1znE&export=download"
gdown.download(url)
shutil.move("./video1.mp4", "./src/video1.mp4")

url = "https://drive.google.com/u/4/uc?id=1U0tvUBod2jJw8dcm-4uE49DGsKPMg4so&export=download"
gdown.download(url)
shutil.move("./video2.mp4", "./src/video2.mp4")

url = "https://drive.google.com/u/4/uc?id=1UDbv-cVPloX7y6vG2aL4IFTYRe1BCmoP&export=download"
gdown.download(url)
shutil.move("./video3.mp4", "./src/video3.mp4")

url = "https://drive.google.com/u/4/uc?id=15sfgAT9gD4e-6-xhwSrrI2kMWXI2kAtL&export=download"
gdown.download(url)
shutil.move("./video4.mp4", "./src/video4.mp4")
