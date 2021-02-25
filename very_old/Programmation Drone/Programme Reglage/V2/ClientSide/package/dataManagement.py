"""
Content the differents functions to get the ground control program work
"""

import cv2
import math


class DataEngine (object):
    """
    Class that threat the data to be used by the client
    """
    def __init__(self):
        pass


    def convertGPSPosition(self, positionStr):
        """
        Convert the GPS given coordinates to latitude and longitude
        """

        positionStr = positionStr.split(',') #"5045.56365,N,00419.98988,E".split(',')

        latitude = str(float(positionStr[0][:2]) + float(positionStr[0][2:])/60) + ' ' + positionStr[1]
        longitude = str(float(positionStr[2][:3]) + float(positionStr[2][3:])/60) + ' ' + positionStr[3]

        return latitude, longitude


    def distanceBetweenGPSPoints(self, altitudeOne = 0, altitudeTwo = 0, positionOne = None, positionTwo = None, GPSPointOne = None, GPSPointTwo = None, GPSCoords = False):
        """
        Calculate the distance between two GPS/LATLON points
        positionOne and positionTwo are tuple of lat,lon
        GPSPointOne and GPSPointTwo are string of GPSCoordinates
        When GPSCoords is True, positionOne and positionTwo are useles, GPSPointOne and GPSPointTwo are used
        Else, positionOne and positionTwo are used
        altitudeOne and altitudeTwo are always used as integer
        """

        if GPSCoords:
            lat1, lon1 = convertGPSPosition(GPSPointOne)
            lat2, lon2 = convertGPSPosition(GPSPointTwo)
        else:
            lat1, lon1 = positionOne
            lat2, lon2 = positionTwo

        # approximate radius of earth in km
        R = 6373.0

        # Coords of pilote
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        alt1 = altitudeOne

        # Coords of drone
        lat2 = radians(lat2)
        lon2 = radians(lon2)
        alt2 = altitudeTwo

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c * 1000

        dalt = abs(alt2 - alt1)
        A2 = (distance**2) + (dalt**2)
        distance = math.sqrt(A2)

        return distance

    def convertKeyPressed(self, key_pressed):
        """
        Convert the ascii value of the pressed key to the key herself
        """

        try:
            conversion = chr(key_pressed)
            print(key_pressed,conversion)

            if key_pressed == 122:       # Z
                print('Front')
            elif key_pressed == 115:     # S
                print('Back')
            elif key_pressed == 113:     # Q
                print('Left')
            elif key_pressed == 100:     # D
                print('Right')
            elif key_pressed == 32:      # SPACE
                print('Up')
            elif key_pressed == 0:       # SHIFT
                print('Down')
            elif key_pressed == 105:     # I
                print('Camera Up')
            elif key_pressed == 107:     # K
                print('Camera Down')
            elif key_pressed == 106:     # J
                print('Rotate Left')
            elif key_pressed == 108:     # L
                print('Rotate Right')
            elif key_pressed == 112:
                int('Stop all commands')

        except ValueError:
            return False