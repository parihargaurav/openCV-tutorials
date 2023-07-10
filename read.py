import cv2 as cv

#img = cv.imread('Pics/cat.jpg')

#cv.imshow('Me', img)

# Reading the videos

capture = cv.VideoCapture('Videos/bakchodi.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    #to avoid indefinitely running the video
    
    if cv.waitKey(3) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()




#cv.waitKey(0)