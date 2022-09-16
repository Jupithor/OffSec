#!/usr/bin/python

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup 

url="http://192.168.210.101"

urllist=[]
urllist.append(url)
urlIsFollowed={}
urlIsFollowed[url]=False
start="http"


#testing with beautilfulSoup
#traverse all the links
for urls in urllist:
    response=requests.request("GET",urls) 
    soup=BeautifulSoup(response.text,features="html.parser")
    a = soup.find_all('a')
    for link in a:
        url=link.get('href')
        if url not in urllist and "192.168.210.101" in url:
            urllist.append(url)
            urlIsFollowed[url] = False
                    #Mark page as has been followed
        urlIsFollowed[url]=True
print(urllist)

#def isFollowedCheck(url):
    #for key in urlIsFollowed.keys():
        #if url != key:
            #return False
        #else:
            #return urlIsFollowed[key]

#for urlno in urllist: 
    ##check if url is followed
    #if not urlIsFollowed[urlno]:
        ##get page
        #page=requests.get(urlno)

        ##read lines in page
        #for line in page.text.split("\n"):
            #if "http" in line and url in line:
                #if "\">" in line:
                    #end = "\">"
                #else:
                    #end = "\" "
                #sliced=line[line.index(start):line.index(end)]
                #if "\"" in sliced:
                    #end = "\""
                    #parsedURL=sliced[sliced.index(start):sliced.index(end)]
                #else:
                    #parsedURL=sliced

                #if parsedURL not in urllist:
                    #urllist.append(parsedURL)
                    #urlIsFollowed[parsedURL] = False

                ##Mark page as has been followed
                #urlIsFollowed[urlno]=True

##print all urls and their status
#for key in urlIsFollowed.keys():
    #print(key+": "+str(urlIsFollowed[key]))
