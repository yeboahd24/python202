#!usr/bin/env/python3

class Float_Fail(float):
	def __init__(self, value: float, unit: str) -> None:
		super().__init__(value)
		self.unit = unit

# s2 = Float_Fail(6.5, "knots")  
# print(s2)  # error because immutable can't have their value changed

# This can be fix with the __new__


class Float_Units(float):
	def __new__(cls, value, unit):
		obj = super().__new__(cls, float(value))
		obj.unit = unit
		return obj

s3 = Float_Units(6.5, "knots")  
# print(s3*2)
print(s3.unit)