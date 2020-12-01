#!usr/bin/env/python3


#Bad way

class A:
	CALLBACK = 	lambda x: x * 2

# print(A.CALLBACK(3)) # works
call =  A()
# print(call.CALLBACK(4)) # WRONG

# God Way

class FunctionHolder:
	def __init__(self, f):
		self._f = f

	def __get__(self, x, y):
		return self._f


class A:
	CALLBACK = FunctionHolder(lambda x: x * 2)


call = A()
print(call.CALLBACK(3))
	