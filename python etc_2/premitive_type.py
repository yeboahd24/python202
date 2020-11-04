#!usr/bin/env/python3

def count_bit(num):
	num_bits = 0
	while num:
		num_bits += num & 1
		num >>= 1
	return num_bits

# print(count_bit(4))



def parity(num):
	"""This check for parity of an integer
		That is is num is odd it returns 0 and even returns 1
	"""
	result = 0
	while num:
		result ^= num & 1
		num >>= 1
	return result

print(parity(2))