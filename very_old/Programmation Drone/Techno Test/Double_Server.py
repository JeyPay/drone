
import socket
import select
import _thread

def server1(local_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket. TCP_NODELAY, 1)

    host = socket.gethostbyname(socket.gethostname())
    print(host)
    port = local_port
    print(port)
    s.bind((host,port))
    s.listen(5)

    c, addr = s.accept()

    while True:
        print(port, c.recv(1024).decode())


_thread.start_new_thread(server1, (5007,))
_thread.start_new_thread(server1, (5008,))
