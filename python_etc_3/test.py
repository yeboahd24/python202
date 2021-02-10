
from collections import namedtuple

Customer = namedtuple('Customer', 'name age')

class Test:
	def __init__(self, customer, age, check=None):
		self.customer = customer
		self.age = age
		self.check = check

	def foo(self):
		return self.customer.age if self.customer.age >18 else 0

	def test(self):
		return self.age + 1

def check(o):
	return o.customer.name+'s'



	


# c = Customer('Linux', 9)
# t = Test(c, 20, check)
# print(t.foo())



# def deco(active=False):
# 	def inner(func):
# 		if active:
# 			print('user is active')
# 		else:
# 			print('user is inactive')
# 		return func
# 	return inner

# @deco(active=True)
# def test():
# 	print('decorator testing...')
# test()

# #Fact(immutabilty)
# x = (1, [1,2])
# y = (1, [1,2])
# print(id(x[-1])) #same
# print(x==y) #True
# x[-1].append(3)
# print(x==y) #False
# print(id(x[-1])) #same

#mutability
# a = [1,2]
# b = [1,2]
# print(id(a[-1]))
# print(a==b) #same
# a.append(3)
# print(a==b)#False
# print(id(a[-1]))#differs


import copy

class Bus:
	def __init__(self, passengers=None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = list(passengers)

	def pick(self, name):
		self.passengers.append(name)

	def drop(self, name):
		self.passengers.remove(name)




# bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
# bus2 = copy.copy(bus1)
# bus3 = copy.deepcopy(bus1)
# print(id(bus1), id(bus2), id(bus3))
# bus1.drop('Bill')
# print(bus2.passengers) # affect bus2 because of the shallow copy
# print(id(bus1), id(bus2), id(bus3))
# print(bus3.passengers) # never change



import weakref

a_set = {0, 1}
a = {'a':'A', 'b':'B'}
x=weakref.WeakKeyDictionary()
x = a
wref = weakref.ref(a_set)
print(wref)
print(wref()) # {0,1}
# a_set = {2, 3, 4} 
# print(wref) # dead(None)
print(x)
