#!/bin/bash

#begining af IP:
IP=$1
#INT of range:
range=$2

lastOct=$(echo $IP | cut -d"." -f4)
firstOcts=$(echo $IP | cut -d"." -f-3)

#do host $IP and filter out "not found"
for x in $(seq $lastOct $range); do host -W 1 -l $firstOcts"."$x $firstOcts"."$x ; done


