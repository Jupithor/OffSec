#!/bin/python
import sys

numberofAs=int(sys.argv[1])
onlyA=b'\x41'
with open("onlyAs.txt","wb") as f:
	f.write(numberofAs*onlyA)
