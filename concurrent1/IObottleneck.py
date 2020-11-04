#!usr/bin/env/python3
import requests

""" I/O bottlenecks, or I/O bottlenecks for short, are bottlenecks where your computer spends
	more time waiting on various inputs and outputs than it does on processing the
	information."""

import urllib.request
import time

# t0 = time.time()
# req = urllib.request.urlopen('http://www.example.com')
# pageHtml = req.read()
# t1 = time.time()
# print("Total Time To Fetch Page: {} Seconds".format(t1-t0))



t0 = time.time()

req = requests.get('https://www.google.com')
pageHtml = req.content
print(pageHtml)

t1 = time.time()
print("Total Time To Fetch Page: {} Seconds".format(t1-t0))
