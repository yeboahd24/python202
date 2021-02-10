#!usr/bin/env/python3

from abstract import Tombola

@Tombola.register # virtual class of Tombola
class TomboList(list):

	def pick(self):
		if self: #
			position = randrange(len(self))
			return self.pop(position) #
		else:
			raise LookupError('pop from empty TomboList')

	load = list.extend

	def loaded(self):
		return bool(self)

	def inspect(self):
		return tuple(sorted(self))



# Note that because of the registration, the functions issubclass and isinstance act as
# if TomboList is a subclass of Tombola:
x = TomboList
y = Tombola
print(issubclass(x, y)) # True
t = TomboList(range(100))
print(isinstance(t, Tombola)) # True
print(TomboList.__mro__)

# Tombola is not in Tombolist.__mro__, so Tombolist does not inherit any methods from
# Tombola.

print(issubclass(x, list))