import cv2
import numpy as np

img = np.zeros((512, 512, 3),np.uint8)
#print(img)
#img[:]= 255,0,0

p1 = (100,200)
p2 = (50,50)
p3 = (300,100)

cv2.line(img, (0, 0), (img.shape[1],img.shape[0]), (0, 255, 0),3)
cv2.line(img, p1, p2, (255,0,0),3)
cv2.line(img, p2, p3, (255,0,0),3)
cv2.line(img, p1, p3, (255,0,0),3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(img, (400, 50),30,(255, 255, 0),5)
cv2.putText(img, ' OPENCV  ', (300, 200), cv2.FONT_HERSHEY_COMPLEX,1,(0, 150, 0),3)


cv2.imshow('Image', img)

cv2.waitKey(0)
