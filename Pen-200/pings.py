import sys
import subprocess

 
#first=sys.argv[1]
#begin=sys.argv[2]
#end=sys.argv[3]

first='127.0.0'
begin=1
end=6

for x in range(begin,end+1):
    host=first+"."+str(x)
    ping=subprocess.call(["ping", "-c1","-w1",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE) == 0
    if ping:
        print(host)