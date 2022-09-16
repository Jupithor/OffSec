#!/usr/bin/python3
#scanner.py

import socket
import time

startTime = time.time()

target_ip= '192.168.188.68'
j=1
k=2
i=0
ssh=False

while not ssh:
    while i<4999:
        i=j*k
        j+=1  
        k+=1
        if(i>4000 and i<4999):
            print('Trying port %d' %(i))
            scanner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            conn = scanner.connect_ex((target_ip,i))
            if(conn==0):
                print('Port %d: OPEN' %(i))
        ssh=True
    #scanner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #conn = scanner.connect_ex((target_ip,2222))
    #if(conn==0):
        #print("ssh open")
        #ssh=True

#for i in range(portstart,portend):
    #scanner.close()

#endTime= time.time()
#totalTime=endTime-startTime
#print('Total time: %s' %(totalTime))