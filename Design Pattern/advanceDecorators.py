from functools import wraps
def my_do_twice_decorator(func):
	wraps(func)
	def new_func(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
	return new_func



@my_do_twice_decorator
def hello_function():
	print('hello from regular functions!')


