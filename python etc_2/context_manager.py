#!usr/bin/env/python3


class ContextIllustration:
	def __enter__(self):
		print('entering context')

	def __exit__(self, exc_type, exc_value, traceback):
		print('leaving context')
		if exc_type is None:
			print('with no error')
		else:
			print(f'with an error ({exc_value})')



# with ContextIllustration():
# 	print('inside')



from contextlib import contextmanager
@contextmanager
def context_illustration():
	print('entering context')
	try:
		yield
	except Exception as e:
		print('leaving context')
		print(f'with an error ({e})')
 # exception needs to be reraised
 
	else:
		print('leaving context')
		print('with no error')


with context_illustration():
	print('inside')
