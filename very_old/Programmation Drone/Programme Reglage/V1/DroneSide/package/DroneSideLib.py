# Lib of DroneSide.py

class ValuesObject (object):
    def __init__ (self, baudrate):
        self.end = False
        self.Kp = 10
        self.Ki = 10
        self.Kd = 10

        self.gyroX = 0
        self.gyroY = 0

        self.accX = 0
        self.accY = 0
        self.accZ = 0

        self.magAngle = 0
        self.setBaudrate(baudrate)


    def setValuesRegulation(self, Kp, Ki, Kd):
        """
        Set Kp, Ki and Kd in the object
        """
        self.Kp = int(Kp)
        self.Ki = int(Ki)
        self.Kd = int(Kd)


    def getValuesRegulation(self):
        return self.Kp, self.Ki, self.Kd


    def setValuesGyro(self, gyroX, gyroY):
        """
        Set gyroX, gyroY in the object
        """
        self.gyroX = int(gyroX)
        self.gyroY = int(gyroY)


    def getValuesGyro(self):
        return self.gyroX, self.gyroY


    def setValuesAcc(self, accX, accY, accZ):
        """
        Set accX, accY and accZ in the object
        """
        self.accX = int(accX)
        self.accY = int(accY)
        self.accZ = int(accZ)


    def getValuesAcc(self):
        return self.accX, self.accY, self.accZ


    def securityCheck(self):
        """
        Function that stop the drone if he is not well placed
        """

        if self.gyroX < -7500 or self.gyroX > 7500:
            return False

        if self.gyroY < -7500 or self.gyroY > 7500:
            return False

        if self.accZ >= 20:
            # If the vertical acceleration si too high
            return False

        return True


    def readMPU(self):
        """
        Function that read the MPU-9250
        """
        gyroX = 0
        gyroY = 0
        accX = 0
        accY = 0
        accZ = 0
        magX = magY = magZ = 0

        self.setValuesGyro(gyroX, gyroY)
        self.setValuesAcc(accX, accY, accZ)
        self.translateMag(magX, magY, magZ)
        

    def setBaudrate(self, baudrate):
        """
        Definie the baudrate to the accelerometer
        """

        pass


    def translateMag(self, magX, magY, magZ):
        """
        Translate values of the magnetometer to a value between 0 and 360
        """
        magAngle = 0
        self.setValuesMag(magAngle)


    def setValuesMag(self, magAngle):
        """
        Set magnetometer angle
        """

        self.magAngle = int(magAngle)


    def getMag(self):
        return self.magAngle