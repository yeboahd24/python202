

class AgeValidator(object):
	"""docstring for Student"""
	def __init__(self, age):
		self._age = age
		self._name = None

	def __get__(self, instance, owner):
		if self._age is None:
			raise ValueError(f'{self._age}: is not set')
		if self._age < 18:
			raise ValueError(f'{self._age} must be greater than or equal to 18')
		return self._age

	def __set_name__(self, name, owner):
		self._name = name

	def __set__(self, instance, value):
		self._age = value



class Client:
	age = AgeValidator(19) # default value for now


	def __init__(self, age):
		self.age = age

	def foo(self):
		return self.age

t = Client(7)
t.age = 2
print(t.foo())

				# Error occures because the AgeValidator is acting as decorator here
				# but you can you use getter and setter property but if you realize that you
				# you will need the validator in most of your class then implement descriptors, that is my
				# openion, so that you can reuse this validator without trying to use getter and setter
				# througout your class.
				# this makes you avoid DRY


		