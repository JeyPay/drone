
from package.socketManagement import *
import _thread as thread
from time import sleep

import cv2
import urllib.request 
import numpy as np

stream=urllib.request.urlopen('http://94.224.62.65:2134/stream.mjpg')
bytes= bytes()

s = ServerSocket(create = False)
s.createSocket(1234, 2)

s.clientAccept(clientName = "Drone1")

"""def client_accept_change_name():
    s.clientAccept()
    name = s.receive(1024)
    s.modifyClientName(None, name)"""

def convertKeyPressed(key_pressed):

    conversion = chr(key_pressed)
    print(key_pressed,conversion)

    if key_pressed == 122:      # Z
        print('Front')
    elif key_pressed == 115:    # S
        print('Back')
    elif key_pressed == 113:    # Q
        print('Left')
    elif key_pressed == 100:     # D
        print('Right')
    elif key_pressed == 32:     # SPACE
        print('Up')
    elif key_pressed == 0:      # SHIFT
        print('Down')
    elif key_pressed == 105:     # I
        print('Camera Up')
    elif key_pressed == 107:     # K
        print('Camera Down')


while True:
    dict_data = s.receiveAll()

    for client_name in dict_data:
        if dict_data[client_name] == 'end':
            s.removeClient(client_name)

    bytes+=stream.read(1024)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
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
                convertKeyPressed(key_pressed)
            except ValueError:
                pass
