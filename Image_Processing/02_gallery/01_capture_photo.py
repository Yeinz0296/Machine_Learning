from sre_constants import SUCCESS
import cv2
import datetime

cam = cv2.VideoCapture(0)

cv2.namedWindow("Webcam")

while True:
    n_time = datetime.datetime.now()

    #To save as HourMinSec
    current_time = n_time.strftime("%H%M%S")
    #To save as YearMonthDayHourMinSec
    #current_time = n_time.strftime("%Y%m%d%H%M%S")

    success, frame = cam.read()
    
    if not success:
        print("failed to grab frame")
        break
    cv2.imshow("Webcam", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = 'Image_Processing/02_gallery/Gallery/capture_photo{}.png'.format(current_time)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

cam.release()

cv2.destroyAllWindows()