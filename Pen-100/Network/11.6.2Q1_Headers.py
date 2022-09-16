#!/usr/bin/python3
#headers

import requests

host="http://192.168.184.68:8080/headers/"
flag=""
for i in range(1,11):
    req=requests.get(host+str(i))
    flag=flag+str(req.headers.get("Flag"))
print(flag)