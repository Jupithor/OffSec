#!/usr/bin/python3
#html parser

from inspect import Parameter
import requests
from bs4 import BeautifulSoup 

#remember the last "/"
host='http://192.168.184.68:8080/login-1/'

#Data to send to server
info={'username': 'thobbes',
      'password': 'leviathan'}

post = requests.post(host,data = info)
#print(post.status_code)
print(post.text)