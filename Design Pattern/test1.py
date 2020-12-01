#!usr/bin/env/python3

# Shared State Pattern

# class GitFetcher(object):
# 	"""This code fectches tags from Git, This is an example of it."""

# 	_current_tag = None

# 	def __init__(self, tag):
# 		self.current_tag = tag


# 	@property
# 	def current_tag(self):
# 		if self._current_tag is None:
# 			raise AttributeError("tag was never set")
# 		return self._current_tag


# 	@current_tag.setter
# 	def current_tag(self, new_tag):
# 		self.__class__._current_tag = new_tag


	# def pull(self):
	# 	print(f"pulling from {self.current_tag}")
	# 	return self.current_tag


# f1 = GitFetcher(0.1)
# f2 = GitFetcher(0.2)
# f1.current_tag = 0.3
# print(f1.pull())
# print(f2.pull())




# Pythonic way

class SharedAttribute:
	def __init__(self, initial_value=None):
		self.value = initial_value
		self._name = None

	def __get__(self, instance, owner):
		if instance is None:
			return self
		if self.value is None:
			raise AttributeError(f"{self._name} was never set")
		return self.value


	def __set__(self, instance, new_value):
		self.value = new_value


	def __set_name__(self, owner, name):
		self._name = name



class GitFetcher:
	current_tag = SharedAttribute()
	current_branch = SharedAttribute()


	def __init__(self, tag, branch=None):
		self.current_tag = tag
		self.current_branch = branch


	def pull(self):
		print(f"pulling from {self.current_tag}")
		return self.current_tag


f1 = GitFetcher(0.4)
f2 = GitFetcher(0.5)
print(f1.pull())
print(f2.pull())