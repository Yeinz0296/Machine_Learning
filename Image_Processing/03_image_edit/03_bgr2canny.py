import cv2
import numpy as np
 
img = cv2.imread('Image_Processing/scr/cat.png')
kernel = np.ones((5,5), np.uint8)
 
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img, 150,200)

cv2.imshow('Canny Image', imgCanny)
cv2.waitKey(0)