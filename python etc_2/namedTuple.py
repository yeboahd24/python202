#!usr/bin/env/python3

from typing import NamedTuple, List, Optional

class Monty(NamedTuple):
	name: str
	age: int

	def get_name(self):
		pass

class Python(Monty):
	sch: str  # this will not work because we can't add another attribute but we can overide methods

	def get_name(self):
		pass

p = Python('linux', 2)
# p = Python('linux', 2, 'python') # error
# print(p)


# def add(item: Optional[int]=None):
# 	return item


# print(add())