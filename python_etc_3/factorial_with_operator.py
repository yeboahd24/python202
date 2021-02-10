#!usr/bin/env/python3

from functools import reduce
from operator import mul

def fact(n):
	return reduce(mul, range(1, n+1))


print(fact(5))
#without functional programming
def fact_1(n):
	if n < 2:
		return n
	return n * fact(n-1)


print(fact_1(5))


