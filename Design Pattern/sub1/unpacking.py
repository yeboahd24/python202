#!usr/bin/env/python3

# Unpacking are normally used in function call


def print_args(*args, **kwargs):
	print(args.__class__.__name__, args,\
		kwargs.__class__.__name__, kwargs)
	
print_args() # prints: tuple () dict {}
print_args(1, 2, 3, a="A") # prints: tuple (1, 2, 3) dict {'a': 'A'}