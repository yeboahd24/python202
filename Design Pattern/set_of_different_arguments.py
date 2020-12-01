#!usr/bin/env/python3

class Contact:
	all_contacts = []

	def __init__(self, name='', email='', **kwargs):
		super().__init__(**kwargs) # this accept key word argument, also the kwargs helps to accept any 
		self.name = name           # additional parameters
		self.email = email
		self.all_contacts.append(self)


class AddressHolder:
	def __init__(self, street='', city='', state='', code='', **kwargs):
		super().__init__(**kwargs)
		self.street = street
		self.city = city
		self.state = state
		self.code = code	


class Friend(Contact, AddressHolder):
	def __init__(self, phone='', **kwargs):
		self.phone=phone # explicit
		super().__init__(**kwargs) # this helps in updating




f1 = Friend(33) # to 33 or update it we use dict(phone=phone) in the super().__init__({'phone':phone})
f1.phone=24

print(f1.__dict__)




