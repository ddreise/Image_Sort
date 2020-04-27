#!/usr/bin/env python3
# Image_Sort.py
#
# Sorts images into new folders by year

import sys
import os
import datetime
import pathlib
import string
import shutil

from stat import *

# Open folder

imageDirectory = pathlib.Path(sys.argv[1])
print ("File to be sorted:", imageDirectory)

# Ensure validity of user input (is it a folder?)
if os.path.exists(imageDirectory):
    print("Path exists")
    if os.path.isdir(imageDirectory):
        print("It is a directory")
    else:
        print("It is not a directory")
        exit()
else:
    print("The path does not exist")
    exit()
# Ask user if folder is correct, if "y" continue, if "n" cancel

# Loop through images
for image in os.scandir(imageDirectory):
    info = image.stat()
    mode = image.stat().st_mode

    # Do if regular file
    if S_ISREG(mode):
        mtime = info.st_mtime

        # Parse information to get month and year
        timestamp = datetime.datetime.fromtimestamp(mtime).strftime('%Y_%B')

        # If directory doesn't exists, create directory with corresponding month and year
        print(imageDirectory / timestamp)
        if not os.path.exists(imageDirectory / timestamp):
            os.mkdir(imageDirectory / timestamp)
            print("Folder created ", imageDirectory / timestamp)

        # Move image into new directory
        print ("Image to be moved: ", / imageDirectory / image)
        print ("Directory to move to: ", / imageDirectory / timestamp)
        shutil.move("C:" / imageDirectory / image, "C:" / imageDirectory / timestamp)


    # Ignore if hidden or unique file
    else:
        print('Skipped')


#   Check image properties (specifically month and year)
#   If no month/year, put into "No Date" folder
#   Put into year/month folder
#   If no folder exists, create one

# end
