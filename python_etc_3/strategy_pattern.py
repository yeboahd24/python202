#!usr/bin/env/python3

# Context
# Provides a service by delegating some computation to interchangeable components
# that implement alternative algorithms.

# Strategy
# The interface common to the components that implement the different algorithms.

# Concrete Strategy
# One of the concrete subclasses of Strategy. FidelityPromo, BulkPromo, and Large
# OrderPromo are the three concrete strategies implemented.


from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem(object):

	def __init__(self, product, quantity, price):
		self.product = product
		self.quantity = quantity
		self.price = price

	def total(self):
		return self.price * self.quantity




class Order(object):     # the Context

	def __init__(self, customer, cart, promotion=None):
		self.customer = customer
		self.cart = list(cart)
		self.promotion = promotion


	def total(self):
		if not hasattr(self, '__total'):
			self.__total = sum(item.total() for item in self.cart)
		return self.__total

	def due(self):
		if self.promotion is None:
			discount = 0
		else:
			discount = self.promotion.discount(self)
		return self.total() - discount


	def __repr__(self):
		fmt = '<Order total: {:.2f} due: {:.2f}>'
		return fmt.format(self.total(), self.due())



class Promotion(ABC): # the Strategy: an abstract base class

	@abstractmethod
	def discount(self, order):
		"""Return discount as a positive dollar amount"""

class FidelityPromo(Promotion): # first Concrete Strategy
	"""5% discount for customers with 1000 or more fidelity points"""

	def discount(self, order):
		return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion): # second Concrete Strategy
	"""10% discount for each LineItem with 20 or more units"""

	def discount(self, order):
		discount = 0
		for item in order.cart:
			if item.quantity >= 20:
				discount += item.total() * .1
		return discount



class LargeOrderPromo(Promotion): # third Concrete Strategy
	"""7% discount for orders with 10 or more distinct items"""

	def discount(self, order):
		distinct_items = {item.product for item in order.cart}
		if len(distinct_items) >= 10:
			return order.total() * .07
		return 0


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
	LineItem('apple', 10, 1.5),
	LineItem('watermellon', 5, 5.0)]

order = Order(joe, cart, FidelityPromo())
print(order)
order_1 = Order(ann, cart, FidelityPromo())
print(order_1)



