#!usr/bin/env/python3

class DB:
	def __init__(self, username, password):
		self.username = username
		self.password = password


	def get_username(self):
		print(f'{self.username}')

# Patch
# Note instead of direct accessing the class we patch,
# patch is normally used in authomative testing, 
# is like hacking
def patch(self):
	print(f'Name: {self.username} Passwd: {self.password}')


DB.patch = patch
db = DB('linux', 900)
# print(db.get_username())
print(db.patch())