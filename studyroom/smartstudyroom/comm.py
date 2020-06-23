import socket
import threading

def transmit(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(ip, 10007)
    data = sock.recv(65535)
    d = data.decode('utf-8')
    print(data.decode('utf-8'))
    sock.close()
    return d 