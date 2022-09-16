#!/usr/bin/python3
#client.py

from fileinput import filename
import socket
import binascii
import re
import mmap
from time import sleep

host = "192.168.80.68"
port = 2002
i=0
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,port)) #connect to client
    connection=True
    print("Connected")
    next=client.recv(1024)
    data=b''
    while (next!=b''):
        data+=next
        next=client.recv(1024)
        i=i+1
    print(len(data))
    sleep(5)
    images=data.split(b'\r\n\r\n')
    for i in range(0,len(images)-1):
        print(i)
        sleep(2)
        pos=images[i].find(b'\r\n')
        print(pos)
        sleep(2)
        fileName = b'flag'+images[i][0:pos]
        print(fileName)
        sleep(2)
        fileCont=images[i][pos+2:-2]
        print(fileCont)
        with open("flag"+str(i)+".jpg",'wb+') as f:
            f.write(fileCont)
except ConnectionRefusedError:
    print ("Connection closed")
    connection=False
