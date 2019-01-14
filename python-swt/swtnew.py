import pillowfight
from PIL import Image
import cv2
import numpy

input_image = Image.open("test2.jpg")
output_img = pillowfight.swt(input_image)
im = numpy.asarray(output_img)
cv2.imwrite('ouut.jpg', im)
print(output_img)