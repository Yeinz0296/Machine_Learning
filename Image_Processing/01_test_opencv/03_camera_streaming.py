import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

if (cap.isOpened() == False):
	print("Error access webcam")

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()