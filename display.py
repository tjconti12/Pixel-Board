#!/usr/bin/env python
import sys
import time
from matrix_config import matrix

from rgbmatrix import graphics

#from modules.image import image_view as image

from modules.text import display_text


canvas = matrix
font = graphics.Font()
font.LoadFont("fonts/4x6.bdf")

white = graphics.Color(255, 255, 255)
#                        x1, y1, x2, y2, color
graphics.DrawLine(canvas, 0, 15, 64, 15, white)

display_text("hello", (255, 0, 0))
display_text("world", (0, 0, 255), 10, 25)
display_text("hola que tal?")

try:
    print("Press CTRL-C to stop")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)








try:
    print("Press CTRL-C to stop")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)