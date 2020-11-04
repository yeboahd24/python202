#!usr/bin/env/python3

from typing import Callable
IntExp = Callable[[int, int], int] # this means two integer values that returns an integer value

class Power1:
	def __call__(self, x: int, n: int) -> int:
		p = 1
		for i in range(n):
			p *= x
		return p
pow1: IntExp = Power1()


# print(pow1(2, 0))




class Power2:
	def __call__(self, x: int, n: int) -> int:
		p = 1
		for i in range(n):
			p *= x
		return p

p = Power2()
print(p(2, 0))