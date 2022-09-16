#!/usr/bin/python3
#html parser

from requests import request
import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup 

#Poolmanager sorts the unsorted
#http = urllib3.PoolManager()
host='http://192.168.99.68:8080'

#GET all links from /crawling
response=request("GET",host+'/crawling') 
soup=BeautifulSoup(response.text,features="html.parser")

#traverse all the links
for link in soup.find_all('a'):
    #GET all the individual pages
    flag=request("GET",host+link.get('href'))
    #Look for the  OS-flag on all the pages
    if "OS" in flag.text:
        print(flag.text)

#---------test stuff------------
#url=urlopen('http://192.168.99.68:8080')
#page=url.read()
#soup=BeautifulSoup(page,features="html.parser")
#response = http.request('GET', url)
#print(response.data.decode('utf-8'))
#print(soup)