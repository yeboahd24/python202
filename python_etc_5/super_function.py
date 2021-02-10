#!usr/bin/env/python3
#This kind of method leads to error
class Base:
	def __init__(self):
		print('Base.__init__')

class A(Base):
	def __init__(self):
		Base.__init__(self)
		print('A.__init__')

class B(Base):
	def __init__(self):
		Base.__init__(self)
		print('B.__init__')

class C(A,B):
	def __init__(self):
		A.__init__(self)
		B.__init__(self)
		print('C.__init__')

# c = C()
# print(c) # duplications

class Base:
	def __init__(self):
		print('Base.__init__')

class A(Base):
	def __init__(self):
		super().__init__()
		print('A.__init__')

class B(Base):
	def __init__(self):
		super().__init__()
		print('B.__init__')

class C(A,B):
	def __init__(self):
		super().__init__() # Only one call to super() here
		print('C.__init__')

b = C()
print(b)
print(C.__mro__)