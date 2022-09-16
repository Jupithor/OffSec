#!/usr/bin/python3
#html parser

import requests

#remember the last "/"
host = 'http://192.168.184.68:8080/basic-post/'

#Data to send to server
info = {'offsec': 'any'}


post = requests.post(host, data = info)
print(post.text)