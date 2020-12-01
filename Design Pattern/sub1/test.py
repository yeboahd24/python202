#!usr/bin/env/python3

class UpperCaseFactory(object):
	def uppercase_string(self, string):
		return string.upper()


class Loader(object):
	def load(string, factory):
		item = factory.uppercase_string(string)
		
		return item


# Test Case:
f = UpperCaseFactory()
result = Loader.load('programming', f)  # PROGRAMMING
# print(result)



class MaximumNumber(object):
	def maximum(self, array):
		default = array[0]
		for num in array:
			if num > default:
				default = num
		return default

class Loader(object):
	def load( array, factory):
		item = factory.maximum(array)
		return item

m = MaximumNumber()
data = [1, 2, 3, 4, 5]
result = Loader.load(data, m)
# print(result)
