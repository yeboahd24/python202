#!usr/bin/env/python3

from functools import wraps

# def dummy_decorator(function):
# 	def wrapped(*args, **kwargs):
# 		Internal wrapped function documentation.
# 		return function(*args, **kwargs)
# 	return wrapped


# @dummy_decorator
# def function_with_important_docstring():
# 	"""This is important docstring we do not want to lose."""


# print(function_with_important_docstring.__name__) # wrapped
# print(function_with_important_docstring.__doc__) # wrapped doc


#To avoid this we have to use the wraps function from the functool


def dummy_decorator(function):
	@wraps(function)
	def wrapped(*args, **kwargs):
		"""Internal wrapped function documentation."""
		return function(*args, **kwargs)
	return wrapped

@dummy_decorator
def function_with_important_docstring():
	"""This is important docstring we do not want to lose."""
print(function_with_important_docstring.__name__)