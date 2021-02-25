# Sol (Client)

from package.socketManagement import *
import cv2
import base64
import numpy as np
import io
from imageio import imread

"""cap = cv2.VideoCapture(0)
retval, image = cap.read()
cap.release()

# Convert captured image to JPG
retval, buffer = cv2.imencode('.jpg', image)

# Convert to base64 encoding and show start of data
jpg_as_text = base64.b64encode(buffer)
print(jpg_as_text[:80])

# Convert back to binary
jpg_original = base64.b64decode(jpg_as_text)

# Write to a file to show conversion worked
with open('test.jpg', 'wb') as f_output:
    f_output.write(jpg_original)"""

class DataCommunication (object):
    """docstring for DataCommunication """
    def __init__(self):
        self.nbBytesMax = 300000
        self.connection = ClientSocket(host = 'localhost', port = 2000, connect = True)


    def receive(self):
        data = self.connection.receive(self.nbBytesMax, decode = False)
        retval, data = cv2.imencode('.jpg', data)
        print(len(data), data)
        return data


    def decodeImage(self, data):
        try:
            jpg_original = base64.b64decode(data)
            jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
            self.image_buffer = cv2.imdecode(jpg_as_np, flags=1)
        except:
            pass


    def displayImage(self):
        try:
            print(self.image_buffer.shape)
            cv2.imshow('ImageClient', self.image_buffer)

        except AttributeError as e:
            print(e)


    def sendDatas(self):
        pass


if __name__ == '__main__':
    connection = DataCommunication()

    bool_run = True
    while bool_run:
        data = connection.receive()
        if data != None:
            connection.decodeImage(data)
            connection.displayImage()

        if cv2.waitKey(1) == 27:
            bool_run = False

        #print(data)