#!/usr/bin/python3
#bijection

from operator import contains
import requests
import json
import itertools
import re

#remember the last "/"
host='http://192.168.184.68:8080/bijection/'

biject=False

i=0

while not biject:

    #Data to send to server

    info={'index': i}
 
    try: 
          post = requests.post(host, data = info)
          #check if everything is ok or raise exception
          post.raise_for_status()
          print(re.findall(r'.*</br></br></br></br></br>',post.text))
          flag=re.findall(r'.*</br></br></br></br></br>',post.text)
          i+=1
          if '}' in flag:
            biject=True
    except requests.exceptions.HTTPError as err:
      print(err)

