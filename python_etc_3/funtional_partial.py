#!usr/bin/evn/python3

from operator import mul
from functools import partial

triple = partial(mul, 3)

print(triple(7))
print(list(map(triple, range(1, 10))))


# def mul_1(n):
# 	return n*3

# m = mul_1(7)
# print(m)

