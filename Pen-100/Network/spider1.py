#!/usr/bin/python3
import requests

URL = "http://192.168.210.101/"
urlList = []
isFollowed = {}

def checkUrlList(URL):
   if URL in urlList:
       return True
   else:
       return False

def isFollowedCheck(URL):
   for entry in isFollowed.keys():
       if URL != entry:
           return False
       else:
           if isFollowed[URL] == "yes":
               return True
           else:
               return False
                               
urlList.append(URL)

for URL in urlList:
   if isFollowedCheck(URL) != True:
       page = requests.get(URL)
       isFollowed[URL] = "yes"
       
       start = "http"
       for line in page.text.split("\n"):
           if "http" in line:
               if "192.168.210.101" in line:
                   if "\">" in line:
                       end = "\">"
                   else:
                       end = "\" "
                   sliced = line[line.index(start):line.index(end)]
                   if "\"" in sliced:
                       end = "\""
                       parsedURL = sliced[sliced.index(start):sliced.index(end)]
                   else:
                       parsedURL = sliced
                   if checkUrlList(parsedURL) == False:
                       urlList.append(parsedURL)
                       isFollowed[parsedURL] = "no"

for URL in urlList:
   print(URL)