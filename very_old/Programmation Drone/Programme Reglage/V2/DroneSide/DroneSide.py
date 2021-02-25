
# Import socketManagement to easily use socket
from package.socketManagement import ServerSocket
# Import the DroneLib script
from package.DroneSideValLib import *
from package.DroneSideElecLib import *
# Multi-threading
import _thread as thread
from time import sleep


class GeneralObject (object):
    def __init__ (self):
        # This object contains all the values that the functions may need
        self.Values = ValuesObject()
        self.Elec = ElecObject()

        # We start 'connectionManagement' as a thread because he is 'blocking'
        thread.start_new_thread(self.connectionManagement, ())
        # We start 'regulate' as a thread because it's very important that he is not dependant of the bugs that other functions can have
        thread.start_new_thread(self.regulate, ())

    def commandTranslate(self, command):
        """
        Function that translate the commands received from the client
        """

        command = eval(command)
        print(command)

        id = command['id']

        if id == 'set':
            self.Values.setRegulation(command['Kp'], command['Ki'], command['Kd'])
            print(self.Values.get())
            #regulate()

        elif id == 'get':
            print(self.Values.getRegulation(), self.Values.getGyro(), self.Values.getAcc())

        elif id == 'end':
            self.stopMotors()
            print('END')
            self.Values.end = True

        """elif id == 'GENERAL_STOP':
            self.Values.setGyro(8000, 8001)
            print('GENERAL_STOP')"""


    def connectionManagement(self):
        """
        Function that get commands from client
        """

        try:
            Connection = ServerSocket(port = 1230, create = True)
        except OSError as e:
            print(e)
            self.Values.end = True

        print('Waiting for client...')
        Connection.clientAccept(clientName='Client1')

        bool_connect = True
        while bool_connect:
            print('Waiting for command...')
            # command = input('Command : ')

            try:
                data_received = Connection.receive('Client1')
                if data_received == '':
                    self.Values.end = True
                    print('Ending bool_connect')

                else:
                    self.commandTranslate(data_received)

            except: pass

            if self.Values.end:
                print("ENDCONNECTION")
                bool_connect = False
                bool_accept = False


    def regulate(self):
        """
        Function that stabilize the drone
        """

        bool_regulate = True
        while bool_regulate:
            # We read the MPU I2C
            self.Values.readMPU()

            # Check if the drone passed the security check
            passed = self.Values.securityCheck()
            if passed:
                # We get regulations values
                Kp, Ki, Kd = self.Values.getRegulation()
                # We get MPU-9250 values
                gyroX, gyroY = self.Values.getGyro()
                accX, accY, accZ = self.Values.getAcc()

                #print('Regulation Values', self.Values.getRegulation())

                # We set values between 0 and 100 for the power in the motors
                self.Elec.setMotors(frontLeft = 0, frontRight = 0, backLeft = 0, backRight = 0)

                # This sleep can be deleted when the function will be slower (read MPU, calculations, ...)
                sleep(0.01)

            elif not passed or self.Values.end:
                # If the security check didn't passed, we end the program
                self.Values.end = True
                print('ENDREGULATE')
                bool_regulate = False


    def daemon(self):
        """
        Function that keep the program alive
        """

        bool_run = True
        while bool_run:
            sleep(0.05)

            if self.Values.end:
                self.stopMotors()
                bool_run = False
                print('ENDRUN')


Program = GeneralObject()
# We start the program
Program.daemon()

# {"id":"set", "Kp":12, "Ki":15, "Kd":18}