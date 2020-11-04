#!usr/bin/env/python3



from functools import wraps
def deco(func):
	@wraps(func)
	def inner(*args):
		result = func(str(*args).upper())
		return result
		# return func(str(*args).upper())
	return inner

@deco
def orig(n):
	print(n)

print(orig('linux'))

