#!usr/bin/env/python3


# Setting an attribute for a function because we can make it as an object

def my_function():
	print("The Function Was Called")
my_function.description = "A silly function"

def second_function():
	print("The second was called")
second_function.description = "A sillier function."


def another_function(function):
	print("The description:", end=" ")
	print(function.description)
	print("The name:", end=" ")
	print(function.__name__)
	print("The class:", end=" ")
	print(function.__class__)
	print("Now I'll call the function passed in")
	function()


another_function(my_function)
another_function(second_function)


# using attribute as a function
class A:

	def print(self):
		print("my class is A")

def fake_print():
	print("my class is not A")

a = A()
a.print() # function , this call both print and fake_print
a.print = fake_print
a.print()