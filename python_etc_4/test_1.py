#!usr/bin/env/python3

def apply_async(func, args, *, callback):
	# Compute the result
	result = func(*args)
	# Invoke the callback with the result
	callback(result)

def get_results(name):
	print(f'My name is {name}')

def get_name(age):
	return age

apply_async(get_name, ('Linux',), callback=get_results)
