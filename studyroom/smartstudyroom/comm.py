import socket
import threading

def transmit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(('192.168.0.11', 10007))
    data = sock.recv(65535)
    d = data.decode('utf-8')
    print(data.decode('utf-8'))
    sock.close()
    return d 