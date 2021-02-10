#!usr/bin/env/python3

class A:
	def ping(self):
		print('ping:', self)

class B(A):
	def pong(self):
		print('pong:', self)

class C(A):
	def pong(self):
		print('PONG:', self)
class D(B, C):
	def pong(self):
		super().pong()  # pythonic
		print('D pong', self)


d = D()

print(d.pong())




