# An HTTP Request in Python

import socket


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('example.com', 80))   # args: domain name and port number
cmd = 'GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n'.encode()
my_socket.send(cmd)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

my_socket.close()
