#!usr/bin/env/python3
import collections

class DoppelDict(dict): # error prone
	def __setitem__(self, key, value):
		super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)
print(dd)   #out: {'one': 1}
dd['two'] = 2
print(dd)   #{'one': 1, 'two': [2, 2]}

# As you can see only [] got duplicated which shouldn't be the case, all should be duplicate


class DoppelDict_2(collections.UserDict): # pythonic way
	def __setitem__(self, key, value):
		super().__setitem__(key, [value] * 2)


dd = DoppelDict_2(one=1)  # all got duplicated
print(dd)   #out: {'one': [1, 1]}
dd['two'] = 2
print(dd)   #{'one': [1, 1], 'two': [2, 2]}
