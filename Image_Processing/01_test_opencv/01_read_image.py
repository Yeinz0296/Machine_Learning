import cv2

# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread('Image_Processing/scr/cat.png')

# DISPLAY
cv2.imshow('Cat',img)
cv2.waitKey(0)