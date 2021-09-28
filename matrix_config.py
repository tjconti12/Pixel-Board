#!/usr/bin/env python
import time

from rgbmatrix import RGBMatrixOptions, RGBMatrix

# Matrix configurations
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options = options)