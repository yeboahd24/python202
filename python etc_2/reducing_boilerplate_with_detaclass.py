#!usr/bin/env/python3

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		"""Add two vectors using + operator"""
		return Vector(
			self.x + other.x,
			self.y + other.y,
		)

	def __sub__(self, other):
		"""Subtract two vectors using - operator"""
		return Vector(
			self.x - other.x,
			self.y - other.y,
		)

	def __repr__(self):
		"""Return textual representation of vector"""
		return f"<Vector: x={self.x}, y={self.y}>"

	def __eq__(self, other):
		"""Compare two vectors for equality"""
		return self.x == other.x and self.y == other.y


# vector = Vector(2, 3)
# print(vector) # repr
# print(vector + Vector(1, 2)) # add




# All this boilerplate can be reduce with dataclass

from dataclasses import dataclass, field

@dataclass
class Vector:
	"""by default dataclass provide __init__, __eq__ and __repr__"""
	x: int
	y: int


	def __add__(self, other):
		"""Add two vectors using + operator"""
		return Vector(
			self.x + other.x,
			self.y + other.y,
		)


	def __add__(self, other):
		"""Add two vectors using + operator"""
		return Vector(
			self.x + other.x,
			self.y + other.y,
		)



vector = Vector(2, 3)
# print(vector) # repr
# print(vector == Vector(1, 4))
# vector.x = 1
# print(vector)




# static typing with dataclass
@dataclass
class DataClassWithDefaults:
	static_default: str = field(default="this is static default value")
	factory_default: list = field(default_factory=list)

data = DataClassWithDefaults()
print(data)