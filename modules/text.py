from PIL import Image
from matrix_config import matrix
from rgbmatrix import graphics

def display_text(text, color = (0, 0, 255), x = 10, y = 10):
    canvas = matrix
    font = graphics.Font()
    font.LoadFont("fonts/4x6.bdf")

    color1 = color[0]
    color2 = color[1]
    color3 = color[2]

    final_color = graphics.Color(color1, color2, color3)

    graphics.DrawText(canvas, font, x, y, final_color, text)

    #display_text("test", (255, 0, 0), 20, 20)
        #text to display
        #color rgba in () default=blue
        #x offset in pixels default=10
        #y offset in pixels default=10