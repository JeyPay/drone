
import cv2
import urllib 
import numpy as np

stream=urllib.urlopen('http://94.224.62.65:2134/stream.mjpg')
bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        cv2.imshow('i',i)
        key_pressed = cv2.waitKey(1)
        if key_pressed == 27:
            exit(0)   
        else:
            try:
                print(key_pressed,chr(key_pressed))
            except ValueError:
                pass
