import time
import sys
from PIL import Image

from matrix_config import matrix

if len(sys.argv) <2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]

image = Image.open(image_file)
image.resize((matrix.width, matrix.height), Image.ANTIALIAS)


double_buffer = matrix.CreateFrameCanvas()
img_width = image.width
img_height = image.height

#scroll
xpos = 0
try:
    print("Press CTRL-C to stop")
    while True:
        xpos +=1
        if (xpos > img_width):
            xpos = 0

        double_buffer.SetImage(image, -xpos)
        double_buffer.SetImage(image, -xpos + img_width)

        double_buffer = matrix.SwapOnVSync(double_buffer)
        time.sleep(0.01)

   
except KeyboardInterrupt:
    sys.exit(0)