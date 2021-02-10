#!usr/bin/env/python3

#first class object-is program that can be,
# * Assign to a variable
# * Created at a runtime
# * Passed as an argument

def factorial(n):
	'''return n'''
	return 1 if n <= 1 else n * factorial(n-1)

# fact = factorial() # as variable
# fact(5)
print(list(map(factorial, range(11)))) # as argument


# High order fucntion-function that takes a function as argument
# Eg: map, sorted, i.e (key)

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
# print(sorted(fruits, key=len))
print(sorted(fruits, key=lambda word: word[::-1])) # reversing

# Explecit way
def reverse(word):
	return word[::-1]