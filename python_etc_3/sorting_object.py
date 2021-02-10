#!usr/bin/env/python3

#Sorting object of the same class

class User(object):
	def __init__(self, user_id):
		self.user_id = user_id

	def __repr__(self):
		return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)   #[User(23), User(3), User(99)]

print(sorted(users, key=lambda u: u.user_id))   #[User(3), User(23), User(99)]


#Instead of using lambda, an alternative approach is to use operator.attrgetter():
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))
#NB: attregetter is a little bit faster than lambda
