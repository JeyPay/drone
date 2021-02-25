# Drone (Serveur)

from package.socketManagement import *
import cv2
import base64
import time

class DataCommunication (object):
    """
    Class that communicate the datas to the ground control program
    """

    def __init__ (self):
        self.nbBytesMax = 300000
        self.connection = ServerSocket(port = 2000, create = True)


    def createVideoThread(self):
        self.cap = cv2.VideoCapture(0)


    def readVideoThread(self):
        retval, image = self.cap.read()

        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer)
        #print(str(jpg_as_text))
        
        return image
        #print(self.jpg_as_text, len(self.jpg_as_text))


    def clientAccept(self):
        if self.connection.nbClients() == 0:
            self.connection.clientAccept(clientName="Client1")


    def completeImageBytes(self, data):
        #nbBytesToComplete = self.nbBytesMax - len(data)
        #data = data.decode() + ''.join([' ' for loop in range(nbBytesToComplete)])

        return data


    def createDataString(self, *data):
        """
        Give all the datas to the object
        """

        dataString = ':'.join(data)
        nbBytesToComplete = self.nbBytesMax - len(self.dataString) - 1

        #print(len(self.dataString),self.dataString)
        return dataString + ''.join([' ' for loop in range(nbBytesToComplete)]) + '/'
        #print(len(self.dataString),self.dataString)


    def sendDatas(self, data):
        print('2',len(data), data)
        self.connection.sendAll(data, dataEncoding=None)

if __name__ == '__main__':
    connection = DataCommunication()
    connection.createVideoThread()

    while True:
        connection.clientAccept()
        packetID = 0
        data = connection.readVideoThread()
        data = connection.completeImageBytes(data)
        
        #data = connection.createDataString(str(packetID),str(124),str(32),str(90),str(240),'5045.56365,N,00419.98988,E')
        connection.sendDatas(data)

        time.sleep(1)

connection.cap.release()