class Mixin(object): # depends on Profile class
	def show_proile(self):
		return f"My name is {self.name} and I'm {self.age} years old"

# Mixins are class that is not meant to be instatiated
# Or class that depends on ther class to work

class Profile(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age


class Work(Profile, Mixin): # aggregate class
	pass


work = Work("Linux", 20)
print(work.show_proile())