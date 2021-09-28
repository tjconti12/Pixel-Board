from PIL import Image
from matrix_config import matrix

def image_view(img, width = matrix.width, height = matrix.height, x = 0, y = 0):
    image = Image.open(img)

    image.thumbnail((width, height), Image.LANCZOS)

    matrix.SetImage(image.convert('RGB'), x, y)

#image_view(cat.jpeg, 20, 20, 10, 10)
    #image path
    #width of img result    default = matrix width
    #height of img result   default = matrix height
    #x offset               default = 0
    #y offset               default = 0


