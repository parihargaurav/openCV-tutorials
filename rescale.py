import cv2 as cv

img = cv.imread('Pics/me.jpg')
cv.imshow('Me', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]+ scale)
    height = int(frame.shape[0]+ scale)
    
    dimensions= (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

#  reading the videos

capture = cv.VideoCapture('Videos/yo.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, scale=.2)
    
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    #to avoid indefinitely running the video
    
    if cv.waitKey(3) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



