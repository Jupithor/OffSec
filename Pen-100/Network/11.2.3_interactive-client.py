#!/usr/bin/python3
#client.py

from re import S
import socket
import telnetlib

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.188.68"
port = 2003

with telnetlib.Telnet(host,port) as tn:
    tn.interact()

client.connect((host,port)) #connect to client
msg = client.recv(1024)
print (msg.decode('ascii'))

client.close()
