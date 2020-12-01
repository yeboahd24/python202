#!usr/bin/env/python3


from threading import Timer
import datetime
import requests
import json

class UpdatedURL:
	"""This fetch data from website every one hour"""
	def __init__(self, url):
		self.url = url
		self.contents = ''
 		self.last_updated = None
 		self.update()

	def update(self):
		self.contents = requests.get(self.url).read()
		self.last_updated = datetime.datetime.now()
 		self.schedule()

	def schedule(self):
		self.timer = Timer(3600, self.update)
		self.timer.setDaemon(True)
		self.timer.start()


u = UpdatedURL("http://news.yahoo.com/")

#Saving to json
json.dupms(u)