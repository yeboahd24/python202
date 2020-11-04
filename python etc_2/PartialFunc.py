#!usr/bin/env/python3


# A prtial function is a generalization of a mathematical function in a way that isn't forced to map
# 	every possible input value (domain) to its results.


from functools import partial
from itertools import count

power_of_2 = partial(pow, 2)
print(power_of_2(4))

infinite_powers_of_2 = tuple(map(partial(pow, 2), count()))
# print(infinite_powers_of_2(1))


