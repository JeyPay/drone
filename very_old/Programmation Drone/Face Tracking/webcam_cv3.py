import cv2
import sys
import datetime as dt
from time import sleep

from imutils import paths
import numpy as np

tolerance = 20
set_point = False

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
anterior = 0

watermark = cv2.imread('small.png', cv2.IMREAD_UNCHANGED)
(wH, wW) = watermark.shape[:2]

(B, G, R, A) = cv2.split(watermark)
B = cv2.bitwise_and(B, B, mask=A)
G = cv2.bitwise_and(G, G, mask=A)
R = cv2.bitwise_and(R, R, mask=A)
watermark = cv2.merge([B, G, R, A])

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)


    """if cv2.waitKey(113) & 0xFF == ord('q'):
        break"""

    if cv2.waitKey(115) & 0xFF == ord('s'):
        save_x = x
        save_y = y
        save_x2 = x+w
        save_y2 = y+h
        save_w = w
        save_h = h
        set_point = True
        print('Points saved')

    if set_point:
        x2 = x + w
        y2 = y + h

        if w > save_w + tolerance:
            print('Back', w - save_w)
        elif w < save_w - tolerance:
            print('Front', save_w - w)
        else:
            print('Distance OK')

        if x < save_x - tolerance:
            print('Left', save_x - x)
        elif y < save_y - tolerance:
            print('Up', save_y - y)
        elif x2 > save_x2 + tolerance:
            print('Right', x2 - save_x2)
        elif y2 > save_y2 + tolerance:
            print('Down', y2 - save_y2)
        else:
            print('Position OK')

    # load the input image, then add an extra dimension to the
    # image (i.e., the alpha transparency)
    #image = cv2.imread(imagePath)
    (h, w) = frame.shape[:2]
    frame = np.dstack([frame, np.ones((h, w), dtype="uint8") * 255])
 
    # construct an overlay that is the same size as the input
    # image, (using an extra dimension for the alpha transparency),
    # then add the watermark to the overlay in the bottom-right
    # corner
    overlay = np.zeros((h, w, 4), dtype="uint8")
    overlay[h - wH - 10:h - 10, w - wW - 10:w - 10] = watermark
 
    # blend the two images together using transparent overlays
    output = frame.copy()
    cv2.addWeighted(overlay, 0.25, output, 1.0, 0, output)
 
    # write the output image to disk
    #filename = imagePath[imagePath.rfind(os.path.sep) + 1:]
    #p = os.path.sep.join((args["output"], filename))
    #cv2.imwrite(p, output)

    cv2.imwrite('output.jpg', output)
    
    # Display the resulting frame
    cv2.imshow('Video', output)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
