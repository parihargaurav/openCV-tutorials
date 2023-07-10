import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#1. Paint the image a certain colour
# blank[200:300 , 300:400] = 0,0,255
# cv.imshow('Green', blank)

# # 2. draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# #3 draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40,  (0,0,250),  thickness=-1)
# cv.imshow('circle', blank)

# #4 draw a line
# cv.line(blank, (100,250), (blank.shape[1]//2, blank.shape[0]//2),  (255,255,255),  thickness=3)
# cv.imshow('line', blank)

# 5. write text

cv.putText(blank, 'Hello Gaurav', (2,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255,0), 2)
cv.imshow('Text', blank)


cv.waitKey(0)