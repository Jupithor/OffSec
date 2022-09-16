#!/usr/bin/python3
#http-sockets.py

import socket

remote_host = "www.megacorpone.com"
remote_port = 80

request = "GET / HTTP/1.1\r\nHost: www.megacorpone.com\r\n\r\n"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((remote_host,remote_port))
client.send(request.encode())

response = client.recv(8192)
print(response.decode())