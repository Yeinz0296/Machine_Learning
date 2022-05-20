# WORK IN PROGRESS

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

def save_video(vid, s_vid):
	n_time = datetime.datetime.now()
	current_time = n_time.strftime("%Y%m%d%H%M%S")
	filename = current_time
	cv2.putText(vid, 'Recording', (75, 40), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
	vid_name = 'Image_Processing/02_gallery/Gallery/record_video{}.mp4'.format(filename)
	result = cv2.VideoWriter(vid_name,cv2.VideoWriter_fourcc(*'MP4V'), 30, size)
	result.write(s_vid)


while True:

	success, frame = cap.read()
	success, s_frame = cap.read()
	frame = cv2.flip(frame, 1)
	s_frame = cv2.flip(s_frame, 1)
	#result.write(frame)
	cv2.putText(frame, 'Not Recording', (75, 40), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,255), 1)
	cv2.imshow('Frame', frame)

	#press R to start record
	if cv2.waitKey(1) & 0xFF == ord('r'):
		save_video(frame, s_frame)
		if cv2.waitKey(1) & 0xFF == ord('s'):
			print("The video was successfully saved")
			break

	elif cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
result.release()

cv2.destroyAllWindows()

#print("The video was successfully saved")
