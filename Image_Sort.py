#!/usr/bin/env python3
# Image_Sort.py
#
# Sorts images into new folders by year

import sys
import os
import datetime

# Open folder
print ("File to be sorted:", sys.argv[1])

imageDirectory = sys.argv[1]

# Ensure validity of user input (is it a folder?)
# Ask user if folder is correct, if "y" continue, if "n" cancel

# Loop through images
for image in os.scandir(imageDirectory):
    info = image.stat()
    mtime = info.st_mtime
    timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
    print('Timestamp: ', str(timestamp_str))
#   Check image properties (specifically month and year)
#   If no month/year, put into "No Date" folder
#   Put into year/month folder
#   If no folder exists, create one

# end
