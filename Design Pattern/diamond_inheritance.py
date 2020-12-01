#!usr/bin/env/python3

class BaseClass:
	num_base_calls = 0

	def call_me(self):
		print("Calling method on Base Class")
		self.num_base_calls += 1


class LeftSubclass(BaseClass):
	num_left_calls = 0

	def call_me(self):
		# BaseClass.call_me(self)
		super().call_me()
		print("Calling method on Left Subclass")
		self.num_left_calls += 1


class RightSubclass(BaseClass):
	num_right_calls = 0

	def call_me(self):
		# BaseClass.call_me(self)
		super().call_me()
		print("Calling method on Rig")


class Subclass(LeftSubclass, RightSubclass):
	num_sub_calls = 0
	def call_me(self):
		# LeftSubclass.call_me(self)
		super().call_me()
	
		# RightSubclass.call_me(self)
		print("Calling method on Subclass")
		self.num_sub_calls += 1



s = Subclass()
print(s.call_me())