#!usr/bin/env/python3

# creating of callable object

class Truncater(object):
	def __init__(self, length):
		# an object is callable if it has __call__ method
		self._length = length


	def __call__(self, size):
		return size[0:self._length]


#Test Case:
print(Truncater(4)('abcdabcd')) # abcd



class Cached:
	def __init__(self, func):
		self._func = func
		self._cache = {}

	def __call__(self, arg):
		if arg not in self._cache:
			self._cache[arg] = self._func(arg)
		return self._cache[arg]
@Cached
def sqr(x):
	return x*x

print(sqr(2))