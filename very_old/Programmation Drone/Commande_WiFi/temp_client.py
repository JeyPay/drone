
import socket               # Import socket module
import select
import time
import os
import shutil
import getpass
import sys


client_path = path = "/Users/ryandanenberg/Desktop" #"/Users/ryandanenberg/Desktop/Programmation/Python/Serveur Python"
server_path = '/'
cmd = ''

plateform = 'Client'

#"94.224.62.65"

host = "localhost" #socket.gethostbyname(socket.gethostname()) #"94.224.62.65" # Get local machine name
print(host)
port = 1234                # Reserve a port for your service.
print(port)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
s.connect((host, port))
# s.settimeout(None)

#s.send(input('Name : ').encode())

bol = True
while bol:
    data = input('data : ')

    if data.split(' ')[0] == 'change':
        s.send(' '.join(data.split(' ')[1:]).encode())

    if data != 'end':
        s.send(data.encode())
    else:
        s.send(b'end')
        bol = False