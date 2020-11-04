#!usr/bin/env/python3

from collections import UserList

class Folder(UserList):
	def __init__(self, name):
		self.name = name

	def dir(self, nesting=0):
		offset = " " * nesting
		print('%s%s/' % (offset, self.name))

		for element in self:
			if hasattr(element, 'dir'):
				element.dir(nesting + 1)
			else:
				print("%s %s" % (offset, element))


# tree = Folder('project')
# tree.append('README.md')
# print(tree.dir())

class MyList(UserList):
	def __init__(self, name):
		self.name = name

	def pops(self, s:int):
		print(f'popping index: {s} from the orginal list {self.name}')
		self.name[s]=None
		if None in self.name:
			self.name.remove(None)
			return f'here is the updated list now {self.name}'

	def appends(self, s:int):
		print(f'appending {s} to the original list {self.name}')
		self.name.append(s)
		return f'updated list {self.name}'





L = MyList([1,2,3,4])
# print(L.pop(1))
print(L.appends(5))