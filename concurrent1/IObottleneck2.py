# import urllib.request
import requests
import time
from bs4 import BeautifulSoup

t0 = time.time()
req = requests.get('http://www.google.com')
t1 = time.time()
print("Total Time To Fetch Page: {} Seconds".format(t1-t0))
soup = BeautifulSoup(req.content, "html.parser")

for link in soup.find_all('a'):
  print(link.get('href'))


t2 = time.time()
print("Total Execeution Time: {} Seconds".format)