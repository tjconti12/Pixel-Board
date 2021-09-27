import base64

img_data = b"place base64 code here"

with open("test64.png", "wb") as fh:
    fh.write(base64.decodebytes(img_data))