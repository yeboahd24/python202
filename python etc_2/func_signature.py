#!usr/bin/env/python3

#Protecting your function signature with kwargs.

def get_process(order, client, payment=True):
	"""This kind of positional args can lead to unespected errors"""
	pass

#using kwargs
def get_process(order, client, *, payment=True):
	"""This means any arguments follow by * must be keyword arguments"""
	pass