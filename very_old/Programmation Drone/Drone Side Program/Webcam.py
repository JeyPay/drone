import cv2
import sys
import datetime as dt
from time import sleep
import base64

video_capture = cv2.VideoCapture(0)

while True:
    """if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass"""

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    gray_img = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)

    retval, buffer = cv2.imencode('.jpg', gray_img)
    jpg_as_text = base64.b64encode(buffer)
    print(len(jpg_as_text))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
