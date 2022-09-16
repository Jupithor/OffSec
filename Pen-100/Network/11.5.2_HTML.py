#!/usr/bin/python3
#web-client

import requests

host = "http://192.168.99.68:8080"
flag=""
for i in range(50):
    url=host+"/"+str(i)+".html"
    response = requests.get(url)
    flag+=response.text.strip()
    #the requests object has many methods - f.eks. .content, .status_code, .header etc.
    
print(flag)
