#!usr/bin/env/python3

# Descriptor attribute for an integer type-checked attribute
class Integer:
	def __init__(self, name):
		self.name = name

	def __get__(self, instance, cls):
		if instance is None:
			return self
		else:
			return instance.__dict__[self.name]

	def __set__(self, instance, value):
		if not isinstance(value, int):
			raise TypeError('Expected an int')
		instance.__dict__[self.name] = value

	def __delete__(self, instance):
		del instance.__dict__[self.name]


class Point:
	x = Integer('x')
	y = Integer('y')

	def __init__(self, x, y):
		self.x = x
		self.y = y

p = Point(2, 3)
p.x # Calls Point.x.__get__(p,Point)
2
p.y = 5 # Calls Point.y.__set__(p, 5)
p.x = 2.3 # Calls Point.x.__set__(p, 2.3)