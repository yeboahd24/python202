#!usr/bin/env/python3

class Decorator:
	"""This decorator affect any instance of the classs"""
	def __init__(self, function):
		self.function = function

	def __call__(self, *args, **kwargs):
		result = self.function(str(*args, *kwargs).upper())
		return result

@Decorator
class Orig:
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

o = Orig('linux')
print(o.name)