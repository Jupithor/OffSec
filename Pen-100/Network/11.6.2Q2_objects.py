#!/usr/bin/python3
#object

import requests

host="http://192.168.184.68:8080/object"


req=requests.get(host)

with open('file','wb') as f:
    f.write(req.content)