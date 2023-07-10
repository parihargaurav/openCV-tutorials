#  5 Essential functions in OpenCv
import cv2 as cv
img= cv.imread('Pics/cat1.jpg')
cv.imshow('cat', img)

# 1 Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2 Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#  3 Edge Cascade

canny = cv.Canny(blur, 125,175)
cv.imshow('Canny Edges', canny)

# 4 Dilating the image
dilated = cv.dilate(canny, (9,9), iterations=3)
cv.imshow('Dilated', dilated)

# 5a Eroding
eroded = cv.erode(dilated, (7,7), iterations= 3)
cv.imshow('Eroded', eroded)

# 5b Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)


# 5c Cropping

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)