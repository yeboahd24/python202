#!usr/bin/env/python3

# This help to avoid encoding error
def bad_filename(filename):
	return repr(filename)[1:-1]
	try:
		print(filename)
	except UnicodeEncodeError:
		print(bad_filename(filename))


# import os
# files = os.listdir('.')

# for f in files:
# 	print(f)


