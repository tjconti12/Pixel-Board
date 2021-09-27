import base64

img_data = b"iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAlklEQVQ4T2NkwAH+H2T/jy7FaP+TEZtyDEG4Zi0TTPXXzoDF0A1DMQRsADbN6MZdO4NiENwQbAbERh1lWLzMmgFGo5iFZBDYEFwuwGsISCPUIKyGgDRjAyBXYXMNIz5XgDQga8TpLboYgux8DO/AwoUuLiEqTLBFMcmxQ7V0gssgklIsLAYozjsoBoE45OZi5DRBSnkCAMLhlPBiQGHlAAAAAElFTkSuQmCC"

# image_64_decode = base64.decodebytes(img_data)
# image_result = open('test_decode.gif', 'wb')
# image_result.write(image_64_decode)

with open("test64.png", "wb") as fh:
    fh.write(base64.decodebytes(img_data))