#!/usr/bin/python3
#server.py

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port=8000

server.bind((host,port))
server.listen(4) # int = the number of clients that can connect

print("Server is running and listening")

while True:
        conn, address = server.accept() #make connection to client
        print("connected to %s" %str(address))
        msg = 'Connection established to %s' %str(host)
        conn.send(msg.encode('ascii'))
        test=conn.recv(1024)
        if not test: continue
        print(test)
        conn.close()