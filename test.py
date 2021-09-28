#!/usr/bin/env python
from python/samples/samplebase import SampleBase


class Test(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            #for x in range(0, self.matrix.width):
             #   offset_canvas.SetPixel(x, x, 255, 255, 255)
              #  offset_canvas.SetPixel(offset_canvas.height - 1 - x, x, 255, 0, 255)

            #for x in range(0, offset_canvas.width):
             #   offset_canvas.SetPixel(x, 0, 255, 0, 0)
              #  offset_canvas.SetPixel(x, offset_canvas.height - 1, 255, 255, 0)

            #for y in range(0, offset_canvas.height):
             #   offset_canvas.SetPixel(0, y, 0, 0, 255)
              #  offset_canvas.SetPixel(offset_canvas.width - 1, y, 0, 255, 0)
            offset_canvas.SetPixel(4, 4, 0, 0, 255)
            offset_canvas.SetPixel(4, 5, 0, 0, 255)
            offset_canvas.SetPixel(4, 6, 0, 0, 255)
            offset_canvas.SetPixel(4, 7, 0, 0, 255)
            offset_canvas.SetPixel(4, 8, 0, 0, 255)
            offset_canvas.SetPixel(5, 6, 0, 0, 255)
            offset_canvas.SetPixel(6, 4, 0, 0, 255)
            offset_canvas.SetPixel(6, 5, 0, 0, 255)
            offset_canvas.SetPixel(6, 6, 0, 0, 255)
            offset_canvas.SetPixel(6, 7, 0, 0, 255)
            offset_canvas.SetPixel(6, 8, 0, 0, 255)

            offset_canvas.SetPixel(8, 4, 0, 0, 255)
            #offset_canvas.SetPixel(8, 0, 0, 0, 255)
            offset_canvas.SetPixel(8, 6, 0, 0, 255)
            offset_canvas.SetPixel(8, 7, 0, 0, 255)
            offset_canvas.SetPixel(8, 8, 0, 0, 255)
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
           


# Main function
if __name__ == "__main__":
    test = Test()
    if (not test.process()):
        test.print_help()
