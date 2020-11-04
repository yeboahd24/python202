#!usr/bin/env/python
# making decorated class if it becomes complicayted
from itertools import starmap
class SavingOrig:
	def __init__(self, another_decorator):
		self._another = another_decorator

	def __call__(self, func):
		print('decorated')
		decorated = self._another(func)
		if hasattr(func, 'orig'):
			decorated.orig = func.orig
		else:
			decorated.orig = func
		return decorated

# print(list(starmap(lambda a, b: a + b, [(1, 2), (3, 4)])))





