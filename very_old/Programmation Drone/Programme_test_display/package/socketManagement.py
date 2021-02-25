
import socket
#import _thread as thread


class ServerSocket (object):
    """
    Give a port and a given number of client to listen and a server will be created
    """
    
    def __init__ (self, port = 1230, listen = 5, create = True):
        self.dictConnectedClient = {}
        if create:
            self.createSocket(port, listen)
        pass


    def createSocket(self, port = 1230, listen = 5):
        """
        Create a socket with a given name and port
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost" #socket.gethostbyname(socket.gethostname()) 
        print(self.host)
        self.port = port
        print(self.port)
        self.listen = listen
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.listen)


    def clientAccept(self, clientName = None):
        """
        Accept a client connection on a given socket name. We can set a name for the client.
        If no client name given, we wait for the client to send his name
        """
        if clientName == None:
            clientName = "None"

        c, addr = self.socket.accept()
        print('Got connection from',addr)
        self.dictConnectedClient[clientName] = [c, addr]


    def receive(self, clientName = "None", nbBytes = 1024, decode = True):
        """
        Receive data from a given client name
        return data received or False if client not connected
        """
        try:
            content = self.dictConnectedClient[clientName][0].recv(nbBytes)
            if decode:
                return content.decode()
            else:
                return content

        except BlockingIOError as e:
            print(e)
            return self.dictConnectedClient[clientName][0].recv(nbBytes).decode()

        except Exception as e:
            print(e)

    def send(self, data, clientName = "None", dataEncoding = 'utf-8'):
        """
        Send a given data to the connected client
        """
        try:
            if dataEncoding != None:
                self.dictConnectedClient[clientName][0].send(data.encode(dataEncoding))
            else:
                self.dictConnectedClient[clientName][0].send(data)

        except BrokenPipeError:
            return clientName

        except OSError:
            pass


    def sendAll(self, data, dataEncoding = 'utf-8'):
        client_to_delete = []
        for clientName in self.dictConnectedClient:
            returned_clientName = self.send(data, clientName=clientName, dataEncoding=dataEncoding)
            if returned_clientName != None:
                client_to_delete.append(returned_clientName)

        for clientName in client_to_delete:
            self.removeClient(clientName)


    def modifyClientName(self, oldClientName, newClientName):
        """
        Modify a given client name to a new given one
        """
        if oldClientName == None:
            oldClientName = "None"

        self.dictConnectedClient[newClientName] = self.dictConnectedClient[oldClientName]
        del self.dictConnectedClient[oldClientName]


    def receiveAll(self, nbBytes = 1024):
        """
        Try to receive data from all connected clients
        """
        dict_data = {}
        list_client_name = list(self.dictConnectedClient)

        for clientName in list_client_name:
            if clientName != "None":
                try:
                    self.dictConnectedClient[clientName][0].settimeout(0)
                    data = self.dictConnectedClient[clientName][0].recv(nbBytes).decode()
                    
                    if data != '':
                        dict_data[clientName] = data
                    else:
                        self.removeClient(clientName)

                    self.dictConnectedClient[clientName][0].settimeout(None)
                except:
                    pass

        return dict_data


    def removeClient(self, clientName):
        """
        Disconnect a client by removing it from the receive dictionnay
        """
        self.dictConnectedClient[clientName][0].settimeout(None)
        del self.dictConnectedClient[clientName]


    def nbClients(self):
        """
        Return the number of clients connected
        """
        return len(self.dictConnectedClient)

class ClientSocket (object):
    """
    Connect to Server Socket as Client
    """

    def __init__(self, host = 'localhost', port = 1230, connect = True):
        if connect:
            self.createSocket(host, port)
        pass


    def createSocket(self, host = 'localhost', port = 1230):
        """
        Create the connection to the given IP and port
        """

        self.host = host
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()


    def connect(self):
        """
        Use the created connection to connect to the Server
        """

        self.connection.connect((self.host, self.port))


    def send(self, data, encode = True):
        """
        Send data to the Server
        """
        if encode:
            self.connection.send(data.encode())
        else:
            self.connection.send(data)


    def receive(self, nbBytes = 1024, decode = True):
        """
        Receive data from the Server
        """
        if decode:
            data = self.connection.recv(nbBytes).decode()
        else:
            data = self.connection.recv(nbBytes)

        return data

    def disconnect(self):
        """
        Disconnect the client from the Server
        """
        
        self.connection.close()

"""
if __name__ == "__main__":

    def WaitClient():
        ServerCommand.clientAccept()
        client_name = ServerCommand.receive()
        ServerCommand.modifyClientName(None, client_name)

    ServerCommand = ServerSocket(port = 1232, listen = 2)

    for loop in range(2):
        WaitClient()

    data = ''
    while data != 'end':
        data_all = ServerCommand.receiveAll()

        for client_name in data_all:
            recvd = data_all[client_name]
            print(ServerCommand.nbClients(), client_name, recvd)
            if recvd == 'end':
                ServerCommand.removeClient(client_name)
                thread.start_new_thread(WaitClient,())"""

