#!/usr/bin/python3
#client.py

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8000

client.connect((host,port)) #connect to server
for i in range(10):
    msg = client.recv(1024)
    print (msg.decode('ascii'))
    client.send(msg)

flag = client.recv(1024)
print (flag.decode('ascii'))
client.close()
