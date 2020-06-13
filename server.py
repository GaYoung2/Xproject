import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('220.67.124.144', 10007))
server_socket.listen(0)
client_socket, addr = server_socket.accept()

data = client_socket.recv(65535)
print("받은 데이터: %s" % data.decode('utf-8'))
data = input("보낼 데이터 입력:")
client_socket.send(data.encode('utf-8'))

client_socket.close()


while True:
    pass