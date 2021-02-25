
import socket

host = "192.168.2.158" #sys.argv[1] # e.g. localhost, 192.168.1.123
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect((host, 5007))

host2 = "192.168.2.158" #sys.argv[1] # e.g. localhost, 192.168.1.123
client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket2.connect((host, 5008))

while True:
    data = input('data : ')

    if data.split(' ')[0] == '1':
        client_socket.send(' '.join(data.split(' ')[1:]).encode())

    else:
        client_socket2.send(' '.join(data.split(' ')[1:]).encode())
