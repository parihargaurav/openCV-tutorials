import cv2 
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('Pics/ball.jpg')
img1= cv2.imread('Pics/ball.jpg')


cv2.imshow('Ball', img)

print(img.shape)
print(img.size)


# define a function to compute and plot histogram

def plot_histogram(img, title, mask=None):
   channels = cv2.split(img)
   colors = ("b", "g", "r")
   plt.title(title)
   plt.xlabel("Bins")
   plt.ylabel("# of Pixels")
   for (channel, color) in zip(channels, colors):
      hist = cv2.calcHist([channel], [0], mask, [256], [0, 256])
      plt.plot(hist, color=color)
      plt.xlim([0, 256])


mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (160, 130), (410, 290), 255, -1)

masked = cv2.bitwise_and(img, img, mask=mask)

plot_histogram(img, "Histogram for Masked Image", mask=mask)


plt.show()
cv2.imshow("Mask", mask)
cv2.imshow("Mask Image", masked)


# equalize histogram

hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


# gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)






cv2.waitKey(0)

