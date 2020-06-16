import socket
import threading

def transmit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(('220.67.124.144', 10007))
    data = input("보낼 데이터 입력:")
    sock.send(data.encode('utf-8'))
    data = sock.recv(65535)
    d = data.decode('utf-8')
    print(data.decode('utf-8'))
    sock.close()
    return d
