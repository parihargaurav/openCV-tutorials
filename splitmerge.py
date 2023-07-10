import cv2 as cv

import numpy as np 
img = cv.imread('Pics/ball.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')
b,g,r= cv.split(img)

blue = cv.merge([b, blank,blank])
green = cv.merge([blank, g,blank])
red = cv.merge([blank, blank,r])



cv.imshow('ball', img)

b, g, r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('green', g)
cv.imshow('red', r)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)

# gray scale images have shape 1