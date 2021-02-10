#!usr/bin/env/python3

import json
from collections import OrderedDict














# how to decode JSON data, preserving its
# order in an OrderedDict:

s = '{"name": "ACME", "shares": 50, "price": 490.1}'

# data = json.loads(s, object_pairs_hook=OrderedDict)
# print(data)

# OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])
class Map:
	def __init__(self, x, y):
		self.x = x
		self.y = y

m = Map(1,2)

print(m.__dict__)





# Here is how you could turn a JSON dictionary into a Python object


# class JSONObject:

# 	def __init__(self, d):
# 		self.__dict__ = d

# data = json.loads(s, object_hook=JSONObject)
# print(data.name) # ACME






# Writing Bytes to a Text File

# import sys

# print(sys.stdout.write(b'Hello\n'))  #error
# print(sys.stdout.buffer.write(b'Hello\n')) # correct

# #The error happens because by default,
# #sys.stdout is always opened in text mode.