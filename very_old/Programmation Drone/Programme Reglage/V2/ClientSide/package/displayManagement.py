"""
Content the differents functions to get the ground control program work
"""

import cv2
import math
import urllib 
import numpy as np


class ImageEngine (object):
    """
    Class that draw all the interface on the stream
    """

    def __init__(self):
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.sizeCircles = 50

        self.readImageThread()
        self.width, self.height = self.getImageSize()


    def readImageThread(self):
        """
        Get image from thread
        """

        self.image =  cv2.imread('temp_image.jpg',1)


    def getImageSize(self):
        """
        Return the current image size
        """

        height, width, channels = self.image.shape

        return width, height


    def configureVideoStreaming(self, url):
        """
        Configure the video streaming
        """

        pass
        """self.stream=urllib.urlopen(url)
        self.bytes=''
        """


    def readVideoStreaming(self):
        """
        Catch image from video streaming and return it
        """

        self.image = cv2.imread('temp_image.jpg', cv2.IMREAD_COLOR)
        """self.bytes+=stream.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            jpg = bytes[a:b+2]
            bytes= bytes[b+2:]
            self.image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        """


    def getImage(self):
        """
        Return the modified (or not) image
        """

        return self.image


    def giveWindowTitle(self, windowTitle):
        """
        Assign the window title to the object
        """

        self.windowTitle = windowTitle


    def displayInterface(self):
        """
        Display the modified window
        """
        cv2.imshow(self.windowTitle, self.image)


    def giveInterfaceValues(self, angleNorth, angleTilt, angleTilt2):
        """
        Function to get values in the object
        """

        self.angleNorth = angleNorth
        self.angleTilt = angleTilt
        self.angleTilt2 = angleTilt2


    def loadInterface(self):
        """
        The main function of the interface drawing
        """

        cv2.rectangle(self.image, (10, 10), (130, 30), (0, 0, 255), cv2.FILLED)
        cv2.putText(self.image, "Battery : 93%", (12, 26), self.font, 0.5, (255, 255, 255), 1)

        cv2.rectangle(self.image, (self.width-10, 10), (self.width-140, 30), (0, 0, 255), cv2.FILLED)
        cv2.putText(self.image, "Altitude : 175m", (self.width-138, 26), self.font, 0.5, (255, 255, 255), 1)

        self.drawCompassNorth(70, 100)
        self.drawDroneTilt(self.width-60, 100)


    def drawDroneTilt(self, centerx, centery):
        """
        Draw the tilt indicator on the image
        """

        posx = centerx
        posy = centery - self.angleTilt2
        self.angleTilt += 90
        x,y = self.calculateCircleAngle(self.angleTilt+180, self.sizeCircles,posx,posy)
        x2,y2 = self.calculateCircleAngle(self.angleTilt+360, self.sizeCircles,posx,posy)
        cv2.line(self.image, (int(x),int(y)), (int(x2),int(y2)), (30,150,250), thickness=2)
        
        for loop in range(-60, 61, 20):
            cv2.line(self.image, (centerx-self.sizeCircles, centery+loop), (centerx+self.sizeCircles, centery+loop), (0,0,255))
            cv2.putText(self.image, str(abs(loop)), (centerx-self.sizeCircles-25,centery+loop+5), self.font, 0.5, (0,0,255), 1)


    def drawCommandDirection(self):
        pass


    def drawCompassNorth(self, posx, posy):
        """
        Draw the compass on the image
        """

        cv2.circle(self.image, (posx,posy), self.sizeCircles, (0,0,255), thickness=2, lineType=8, shift=0)

        x,y = self.calculateCircleAngle(self.angleNorth,self.sizeCircles-10,posx,posy)
        cv2.line(self.image, (posx,posy), (int(x),int(y)), (0,0,255), thickness=2)


    def calculateCircleAngle(self, angle, size, posx, posy):
        """
        Calculate the position of a point on a circle
        """

        x = math.sin(math.radians(angle))*size+posx
        y = -math.cos(math.radians(angle))*size+posy

        return x, y