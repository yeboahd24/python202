#!usr/bin/env/python3

# Duck typing

class OddContainer:
	def __contains__(self, x): # list, set, dict etc 
		if not isinstance(x, int) or not x % 2:
			return False
		return True


odd = OddContainer()
print(1 in odd) # True
print(2 in odd) # False


