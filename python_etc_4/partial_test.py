#!usr/bin/env/python3

def spam(a, b, c, d):
	print(a, b, c, d) 

# print(spam(1)) #error to avoid this use partial

from functools import partial

s1 = partial(spam, 1) 
print(s1) #1

s1(4, 5, 6) #no error
