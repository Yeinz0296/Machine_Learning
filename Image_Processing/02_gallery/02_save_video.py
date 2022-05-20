import cv2
import datetime

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

if (cap.isOpened() == False):
	print("Error access webcam")

size = (frameWidth, frameHeight)

n_time = datetime.datetime.now()
current_time = n_time.strftime("%Y%m%d%H%M%S")

filename = current_time
vid_name = 'Image_Processing/02_gallery/Gallery/save_video_{}.mp4'.format(filename)

result = cv2.VideoWriter(vid_name,cv2.VideoWriter_fourcc(*'MP4V'), 30, size)

while True:
	success, frame = cap.read()
	frame = cv2.flip(frame, 1)
	result.write(frame)
	cv2.imshow('Frame', frame)

	#press S to save
	if cv2.waitKey(1) & 0xFF == ord('s'):
		break

cap.release()
result.release()

cv2.destroyAllWindows()

print("The video was successfully saved")
