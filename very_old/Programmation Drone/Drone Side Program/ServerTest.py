
from socketManagement import *

connection = ServerSocket(port = 1230, create = True)


while True:
    connection.clientAccept(clientName="client")

    while True:
        data = connection.receive(clientName="client", nbBytes=131072, decode=True)
        print(data)

    connection.removeClient(clientName="client")