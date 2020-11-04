#!usr/bin/env/python3

"""Proxy decorators are used to tag and register functions with a global mechanism"""


class User(object):
	def __init__(self, roles):
		self.roles = roles

class Unauthorized(Exception):
	pass



def protect(role):
	def _protect(function):
		def __protect(*args, **kw):
			user = globals().get('user')
			if user is None or role not in user.roles:
				raise Unauthorized("I won't tell you")
			return function(*args, **kw)
		return __protect
	return _protect


tarek = User(('admin', 'user'))
bill = User(('user',))
class RecipeVault(object):

	@protect('admin')
	def get_waffle_recipe(self):
		print('use tons of butter!')

my_vault = RecipeVault()
user = tarek
print(my_vault.get_waffle_recipe())
user = bill
print(my_vault.get_waffle_recipe())