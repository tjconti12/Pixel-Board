import time
import sys
from matrix_config import matrix
from rgbmatrix import graphics

offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("fonts/7x13.bdf")
textColor = graphics.Color(255, 255, 0)
pos = offscreen_canvas.width
my_text = "The text to scroll across the screen"

try:
    print("Press CTRL -C to stop")
    while True:
        offscreen_canvas.Clear()
        len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
        pos -= 1
        if (pos + len < 0):
            pos = offscreen_canvas.width
        
        time.sleep(0.05)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)


except KeyboardInterrupt:
    sys.exit(0)