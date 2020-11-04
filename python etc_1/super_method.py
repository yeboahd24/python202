#!usr/bin/env/python3

#super is a built-in class that can be used to access an attribute belonging to an object's superclass.

class Mama: # this is the old way
	def says(self):
		print('do your homework')


# class Sister(Mama):
# 	def says(self):
# 		Mama.says(self)  # Old way
# 		print('and clean your bedroom')


class Sister(Mama):
	def says(self):
		super().says()
		print('and clean your bedroom')


# sister = Sister()
# print(sister.says())



class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings

	def __repr__(self):
		return "Pizza with " + " and ".join(self.toppings)

	@classmethod
	def recommend(cls):
		"""Recommend some pizza with arbitrary toppings,"""
		return cls(['spam', 'ham', 'eggs'])




class VikingPizza(Pizza):

	@classmethod
	def recommend(cls):
		"""Use same recommendation as super but add extra spam"""
		# recommended = super(VikingPizza).recommend()
		# recommended.toppings += ['spam'] * 5
		# return recommended
		recommended = super().recommend()
		recommended.toppings += ['spam'] * 5
		return recommended



vik = VikingPizza('sam')
print(vik.recommend())