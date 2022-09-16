#!/usr/bin/python3
#html parser

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup 

host='http://192.168.99.68:8080'

#GET the table from /table
response=requests.request("GET",host+'/table') 
soup=BeautifulSoup(response.text,features="html.parser")
flag=''

#Find all rows
for row in soup.find_all('td'):
    flag+=row.text
print(flag)