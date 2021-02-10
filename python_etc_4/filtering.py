#!usr/bin/env/python3


# Sometimes, the filtering criteria cannot be easily expressed in a list comprehension or
# generator expression. For example, suppose that the filtering process involves exception
# handling or some other complicated detail. For this, put the filtering code into its own
# function and use the built-in filter() function. For example:

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']

# filter() creates an iterator, so if you want to create a list of results, make sure you also
# use list() as shown.
# 	
