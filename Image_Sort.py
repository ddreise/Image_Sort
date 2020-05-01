#!/usr/bin/env python3
# Image_Sort.py
#
# Sorts images into new folders by year
# 
# By:   Daniel Dreise
# Date: April 2020
#

import sys
import os
import datetime
import pathlib
import string
import shutil

from stat import *
from pathlib import Path

# Open folder
imageDirectory = pathlib.Path(sys.argv[1])

# Ensure validity of user input (is it a folder?)
if os.path.exists(imageDirectory):
    if not os.path.isdir(imageDirectory):
        print("It is not a directory")
        exit()
else:
    print("The path does not exist")
    exit()

# Ask user if folder is correct, if "y" continue, if "n" cancel
temp = input("Is this the correct folder to sort (<y> or <n>)? : {} ".format(imageDirectory))
if temp != "y":
    print("You've chosen 'no', exitting program.")
    exit()

else:
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
            if not os.path.exists(imageDirectory / timestamp):
                os.mkdir(os.path.join(imageDirectory, timestamp, ))
                print("Folder created: ", os.path.join(imageDirectory, timestamp, ))

            # Move image into new director
            print ("Moving {} to {}".format(image, os.path.join(imageDirectory, timestamp)))
            shutil.move(os.path.join(imageDirectory, image), os.path.join(imageDirectory, timestamp))


        # Ignore if hidden or unique file
        else:
            print('{} skipped'.format(image))

# end
