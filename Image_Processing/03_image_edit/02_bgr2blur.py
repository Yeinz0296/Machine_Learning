import cv2
import numpy as np
 
img = cv2.imread('Image_Processing/scr/cat.png')
kernel = np.ones((5,5), np.uint8)

imgBlur = cv2.GaussianBlur(img, (7,7), 0)

cv2.imshow('Blur Image', imgBlur)
cv2.waitKey(0)