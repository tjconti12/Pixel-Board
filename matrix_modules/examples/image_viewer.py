#!/usr/bin/env python
import time
import sys

from matrix_config import matrix

#Required for image
from PIL import Image

if len(sys.argv) <2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]

image = Image.open(image_file)



# Make image fit screen
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

matrix.SetImage(image.convert('RGB'))

try:
    print("Press CTRL-C to stop")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)