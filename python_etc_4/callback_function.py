#!usr/bin/env/python3
#Extra state with callback function

def apply_async(func, args, *, callback):
	# Compute the result
	result = func(*args)
	# Invoke the callback with the result
	callback(result)


def print_result(result):
	print('Got:', result)

def add(x, y):
	return x + y


def make_handler():
	sequence = 0
	def handler(result):
		nonlocal sequence
		sequence += 1
		print('[{}] Got: {}'.format(sequence, result))
	return handler

apply_async(add, (2, 3), callback=print_result)
# apply_async(add, ('hello', 'world'), callback=print_result)
handler = make_handler()
apply_async(add, (2, 3), callback=handler)