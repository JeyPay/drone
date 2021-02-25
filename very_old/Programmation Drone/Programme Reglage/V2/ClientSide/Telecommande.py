
from package.displayManagement import *
from package.communicationManagement import *
from package.dataManagement import *

import cv2
import urllib.request
import numpy as np

import _thread as thread
from time import sleep
from random import randint

# camera_img = cv2.imread('temp_image.jpg',1)
# height, width, channels = camera_img.shape

connection = CommunicationEngine()
Data = DataEngine()

Image = ImageEngine()
Image.configureVideoStreaming("192.168.2.132:12345/stream.mjpg")
Image.giveWindowTitle("Interface de commande")

angleNorth = 45
angleTilt = angleTilt2 = 25

bool_run = True
while bool_run:

    Image.readVideoStreaming()
    Image.giveInterfaceValues(angleNorth, angleTilt, angleTilt2)
    Image.loadInterface()
    Image.displayInterface()

    key_pressed = cv2.waitKey(1)
    if key_pressed == 27:
        bool_run = False

    Data.convertKeyPressed(key_pressed)