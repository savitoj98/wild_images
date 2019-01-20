# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 20:09:20 2019

@author: Savitoj
"""

import pillowfight
from PIL import Image
from PIL import ImageOps
import cv2
import numpy
import matplotlib.pyplot as plt

input_image = Image.open("New-Folder/img (48).jpg")
#input_image = ImageOps.invert(input_image)
output_img = pillowfight.swt(input_image)
im = numpy.asarray(output_img)

cv2.imwrite("out_img.jpg", im)
mser = cv2.MSER_create()
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
for row in range(len(gray)):
    for col in range(len(gray[0])):
        if row==0 or col==0 or row==len(gray)-1 or col==len(gray[0])-1:
            continue
            
        btm = gray[row+1][col]
        top = gray[row-1][col]
        lft = gray[row][col+1]
        right = gray[row][col-1]
            
        if btm==top and lft==right and lft==0 and top==0:
            gray[row][col] = btm

regions, bboxes = mser.detectRegions(gray)

#cv2.polylines(gray, hulls, 1, (0,100,100), 2)
#cv2.imwrite('amit.jpg', gray)
#plt.imshow(im)

i=0
z = numpy.zeros((len(bboxes), 1))
bboxes = numpy.append(bboxes, z, axis=1)
for p in bboxes:
    bboxes[i][4]=int(round(p[1]/(len(gray[0])//10))*((len(gray[0])//10)))
    i = i+1

bboxes = sorted(bboxes,key=lambda x: (x[4],(x[1]+x[0])))
i=0
for p in bboxes:
    new_img = gray[ int(p[1]) : int(p[1]+ p[3]) , int(p[0]) : int(p[0]+p[2]) ]
    new_img = cv2.copyMakeBorder(new_img,40,40,40,40,cv2.BORDER_CONSTANT,value=[255,255,255]) 
    cv2.imwrite(str(i)+".jpg", new_img)
    i+=1
print("done"+str(i))