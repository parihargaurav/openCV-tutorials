#  Color spacing

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Pics/ball.jpg')
cv.imshow('Ball', img)

# plt.imshow(img)
# plt.show()

#  BGR to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#  bgr to hsv 

hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#  bgr to l+a+b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

cv.imshow('LAB', lab)

#  bgr to rgb

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# hsv to bgr

hsv_bgr= cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV--> BGR', hsv_bgr)

plt.imshow(rgb)

plt.show()

cv.waitKey(0)
#  here we cant convert gray to hsv here we have to convert gray to bgr then bgr to hsv ok