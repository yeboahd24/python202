#!usr/bin/env/python3

import re
class EmailValidatorMixin(object):
	EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+\.[^@]+")
	def __init__(self, email, *args, **kwargs):
		self.email = email if re.match(self.EMAIL_FORMAT, email) else 'Invalid'
		super().__init__(*args, **kwargs)

	def __repr__(self):
		return self.email

# class UserValidatorMixin(object):
# 	USER_FORMAT = 	re.compile(r"!@\?\w+")



class User(EmailValidatorMixin):
	pass

user = User('linux@gmail.com')
# print(user.email)
print(user)


# user1 = re.compile(r"\@!?\w+")
# x = user1.search('linux')
# print(x)