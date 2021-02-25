# Lib of DroneSide.py
import smbus    #library link: https://pypi.org/project/smbus2/
import time
from math import atan, pi

class ElecObject (object):
    def __init__ (self):
        pass


    def setMotors(self, frontLeft = 0, frontRight = 0, backLeft = 0, backRight = 0):
        """
        Function that set a percentage of power on each motor
        """
        #print('Motors percentages :', frontLeft, frontRight, backLeft, backRight)
        pass


    def setCamera(self, height = 50):
        """
        Set camera height with a value between 0 and 100 (PWM)
        """
        pass