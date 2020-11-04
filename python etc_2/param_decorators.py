#!usr/bin/env/python3


def repeat(number=3):
	"""Cause decorated function to be repeated a number of times.
 	Last value of original function call is returned as a result.
 	:param number: number of repetitions, 3 if not specified
 	"""

	def actual_decorator(function):
		def wrapper(*args, **kwargs):
			result = None
			for _ in range(number):
				result = function(*args, **kwargs)
			return result
		return wrapper
	return actual_decorator




@repeat(2) # default=3
def print_my_call():
	print("print_my_call() called!")

# print_my_call()



# def rep(n=3):
# 	def actual(func):
# 		def inner(*args, **kwargs):
# 			for _ in range(n):
# 				result = func(*args, **kwargs)
# 			return result
# 		return inner
# 	return actual

# @rep()
# def name():
# 	print('Linux')
# name()
