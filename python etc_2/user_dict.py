#!usr/bin/env/python3


from collections import UserDict

class DistinctError(ValueError):
	"""Raised when duplicate value is added to a distinctdict."""


class distinctdict(UserDict):
	"""Dictionary that does not accept duplicate values."""
	def __setitem__(self, key, value):
		if value in self.values():
			if (
				(key in self and self[key] != value) or
				key not in self
			):
				raise DistinctError(
				"This value already exists for different key"
			)
		super().__setitem__(key, value)


my = distinctdict()
my['key'] = 'value'
# my['other_key'] = 'value'   #error because the same value
my['key1'] = 'value2'
# print(my)




# Python program to demonstrate 
# userdict 



# Creating a Dictionary where 
# deletion is not allowed 
class MyDict(UserDict): 
	
	# Function to stop deleltion 
	# from dictionary 
	def __del__(self): 
		raise RuntimeError("Deletion not allowed") 
		
	# Function to stop pop from 
	# dictionary 
	def pop(self, s = None): 
		raise RuntimeError("Deletion not allowed") 
		
	# Function to stop popitem 
	# from Dictionary 
	def popitem(self, s = None): 
		raise RuntimeError("Deletion not allowed") 
	
# Driver's code 
d = MyDict({'a':1, 
	'b': 2, 
	'c': 3}) 

print("Original Dictionary") 
print(d) 


