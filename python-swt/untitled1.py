# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 20:09:20 2019

@author: Savitoj
"""

import pillowfight
from PIL import Image
import cv2
import numpy

input_image = Image.open("test.jpg")
output_img = pillowfight.swt(input_image)
im = numpy.asarray(output_img)

mser = cv2.MSER_create()
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
regions, bboxes = mser.detectRegions(gray)

hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
#cv2.polylines(gray, hulls, 1, (0,100,100), 2)
#cv2.imwrite('amit.jpg', gray)
i=0
for p in bboxes:
    cv2.imwrite(str(i)+".jpg", gray[ p[1] : p[1]+ p[3] , p[0] : p[0]+p[2] ])
    i+=1
    