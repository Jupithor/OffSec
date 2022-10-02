#!/bin/python3
import sys

i=int(sys.argv[1])
payload=b'\x41'* i

with open("onlyAs.txt","wb") as f:
	f.write(payload)
