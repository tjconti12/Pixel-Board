import sys
import time
from matrix_config import matrix

from rgbmatrix import graphics

canvas = matrix
font = graphics.Font()
font.LoadFont("fonts/4x6.bdf")

red = graphics.Color(255, 0, 0)
#                        x1, y1, x2, y2, color
#graphics.DrawLine(canvas, 5, 5, 22, 13, red)

green = graphics.Color(0, 255, 0)
#graphics.DrawCircle(canvas, 15, 15, 10, green)

blue = graphics.Color(0, 0, 255)
#canvas to draw to, the font, left, top, color, text
graphics.DrawText(canvas, font, 5, 10, blue, "Test")




try:
    print("Press CTRL-C to stop")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)