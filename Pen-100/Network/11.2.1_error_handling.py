#!/usr/bin/python3
#client.py

import socket

host = "192.168.80.68"
port = 2001


i=0

while i < 10:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host,port)) #connect to client
        i=i+1
        flag = client.recv(1024)
        client.send(flag)
        print (flag.decode('ascii'))
        print("Connected successfull",i,"times")
        if(i!=10):
            client.close()
    except ConnectionRefusedError:
        print ("Connection refused, ", i ,"connections made")

flag = client.recv(1024)
print (flag.decode('ascii'))
client.close()
