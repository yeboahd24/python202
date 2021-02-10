# closures emulate instances of a class
import sys
class ClosureInstance:
	def __init__(self, locals=None):
		if locals is None:
			locals = sys._getframe(1).f_locals

		# Update instance dictionary with callables
		self.__dict__.update((key,value) for key, value in locals.items()if callable(value) )

	# Redirect special methods
	def __len__(self):
		return self.__dict__['__len__']()

# Example use
def Stack():
	items = []


	def push(item):
		items.append(item)

	def pop():
		return items.pop()

	def __len__():
		return len(items)
	return ClosureInstance()

s = Stack()
s.push(10)
s.push(20)
s.push('Hello')
print(len(s)) # 3




class Stack2:
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def __len__(self):
		return len(self.items)