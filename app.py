from ForestFireSegmentation.ForestFireSegmentation import ForestFireSegmentation
from tkinter import messagebox
import tkinter as tk
import numpy as np
import mimetypes
import argparse
import cv2

# Define Constanta Variable
LOWER_VALUE = np.array((82, 0, 159), dtype="uint8")
UPPER_VALUE = np.array((255, 255, 255), dtype="uint8")
METHOD = "lab"
SOURCE_VIDEO = "./test_videos/video1.mp4"
HIGH_AREA_FIRE = 7000
MEDIUM_AREA_FIRE = 3500
LOW_AREA_FIRE = 100

# Define Variable
total_large_of_fire = []

# Set Argument Parse
parser = argparse.ArgumentParser()
parser.add_argument(
    "-l",
    "--lower",
    nargs="+",
    default=LOWER_VALUE,
    type=int,
    help="Input your lower bound value",
)
parser.add_argument(
    "-u",
    "--upper",
    nargs="+",
    default=UPPER_VALUE,
    type=int,
    help="Input your upper bound value",
)
parser.add_argument(
    "-m",
    "--method",
    default=METHOD,
    help="Input your color space method",
)
parser.add_argument(
    "-haf",
    "--high-area-fire",
    type=int,
    default=HIGH_AREA_FIRE,
    help="Input your minimal value to detect high area fire",
)
parser.add_argument(
    "-maf",
    "--medium-area-fire",
    type=int,
    default=MEDIUM_AREA_FIRE,
    help="Input your minimal value to detect medium area fire",
)
parser.add_argument(
    "-laf",
    "--low-area-fire",
    type=int,
    default=LOW_AREA_FIRE,
    help="Input your minimal value to detect low area fire",
)
parser.add_argument(
    "-v",
    "--video",
    default=SOURCE_VIDEO,
    help="Input your video source",
)
parser.add_argument(
    "-ffv",
    "--forest-fire-video",
    default="true",
    help="Forest fire video True or False",
)
value_parser = parser.parse_args()

# Check Value Lower and Upper Bound
if len(value_parser.lower) != 3 or len(value_parser.upper) != 3:
    raise "Input upper bound and lower bound values correctly!"
for i in value_parser.lower:
    if i < 0:
        raise "Input upper bound and lower bound values correctly!"
for i in value_parser.upper:
    if i < 0:
        raise "Input upper bound and lower bound values correctly!"
value_parser.lower = np.array(tuple(value_parser.lower), dtype="uint8")
value_parser.upper = np.array(tuple(value_parser.upper), dtype="uint8")

# Check High Area of Fire
if value_parser.high_area_fire < 0 or value_parser.medium_area_fire < 0 or value_parser.low_area_fire < 0:
    raise "Input your area fire correctly!"

# Check Format Video
mimetypes.init()
mimestart = mimetypes.guess_type(value_parser.video)[0]
if mimestart != None:
    mimestart = mimestart.split("/")[0]
    if mimestart not in ["video"]:
        raise "Input video source correctly!"

# Check Forest Fire Video Statement
if value_parser.forest_fire_video.lower() == "false":
    value_parser.forest_fire_video = False
elif value_parser.forest_fire_video.lower() == "true":
    value_parser.forest_fire_video = True
else:
    raise "Input your forest fire video is True or False!"

# Make Function to Stack Images
def stack_images(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rowsAvailable = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(
                        img_array[x][y], (0, 0), None, scale, scale
                    )
                else:
                    img_array[x][y] = cv2.resize(
                        img_array[x][y],
                        (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                        None,
                        scale,
                        scale,
                    )
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(
                    img_array[x],
                    (img_array[0].shape[1], img_array[0].shape[0]),
                    None,
                    scale,
                    scale,
                )
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


# Make Class Forest Fire Segmentation
ffs = ForestFireSegmentation(
    value_parser.lower, value_parser.upper, value_parser.method
)

# Read Video
cap = cv2.VideoCapture(value_parser.video)

while True:
    # Read Img
    success, img = cap.read()
    img = cv2.resize(img, (550, 250))
    img_draw = img.copy()

    # Preprocessing Image
    img_preprocessing, fire_mask = ffs.preprocessing_image(img)

    # Get Large Area of Fire
    large_of_fire = ffs.get_large_of_fire(img_preprocessing)
    total_large_of_fire.append(large_of_fire)

    # Draw Large Area of Fire
    ffs.draw_large_of_fire(img_preprocessing, img_draw)

    # Check Fires
    if value_parser.forest_fire_video:
        if large_of_fire > value_parser.high_area_fire:
            cv2.rectangle(img_draw, (20, 20), (230, 85), (0, 255, 0), cv2.FILLED)
            cv2.putText(
                img_draw,
                f"{round(large_of_fire)}",
                (30, 70),
                cv2.FONT_HERSHEY_PLAIN,
                1.5,
                (0, 0, 255),
                2,
            )
            cv2.putText(
                img_draw,
                "Big Forest Fire",
                (30, 47),
                cv2.FONT_HERSHEY_PLAIN,
                1.5,
                (0, 0, 255),
                2,
            )
        elif large_of_fire > value_parser.medium_area_fire:
            cv2.rectangle(img_draw, (20, 20), (280, 85), (0, 255, 0), cv2.FILLED)
            cv2.putText(
                img_draw,
                f"{round(large_of_fire)}",
                (30, 70),
                cv2.FONT_HERSHEY_PLAIN,
                1.5,
                (0, 0, 255),
                2,
            )
            cv2.putText(
                img_draw,
                "Medium Forest Fire",
                (30, 47),
                cv2.FONT_HERSHEY_PLAIN,
                1.5,
                (0, 0, 255),
                2,
            )
        elif large_of_fire > value_parser.low_area_fire:
            cv2.rectangle(img_draw, (20, 20), (255, 85), (0, 255, 0), cv2.FILLED)
            cv2.putText(
                img_draw,
                f"{round(large_of_fire)}",
                (30, 70),
                cv2.FONT_HERSHEY_PLAIN,
                1.5,
                (0, 0, 255),
                2,
            )
            cv2.putText(
                img_draw,
                "Small Forest Fire",
                (30, 47),
                cv2.FONT_HERSHEY_PLAIN,
                1.5,
                (0, 0, 255),
                2,
            )

    # Stack Images
    img_result = stack_images(1, ([img, fire_mask], [img_preprocessing, img_draw]))

    # Show Result
    cv2.imshow("Forest Fire", img_result)

    # Check Exit
    if cv2.waitKey(1) == ord("q"):
        break


# Stop All Windows
cap.release()
cv2.destroyAllWindows()

# Display Total Large of Fire
if value_parser.forest_fire_video:
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Info", f"Total large of fire is {round(sum(total_large_of_fire))}")