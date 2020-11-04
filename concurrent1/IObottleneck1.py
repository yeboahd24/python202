# import urllib2
import requests
import time
from bs4 import BeautifulSoup

linkArray = []

def getLinks():
  req = requests.get('http://www.google.com')
  soup = BeautifulSoup(req.content, 'html.parser')
  for link in soup.findAll('a'):
    linkArray.append(link.get('href'))
    print(len(linkArray))

getLinks()