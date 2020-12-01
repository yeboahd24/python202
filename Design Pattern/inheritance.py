#!usr/bin/env/python3

# Extending list class
class ContactList(list):
	def search(self, name):
		'''Return all contacts that contain the search value in their name.'''
		matching_contacts = []
		for contact in self: # the class it self
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts 

class Contact(object):
	all_contacts = ContactList()

	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.all_contacts.append(self)




# class Contact(object):
# 	all_contacts = [] # class variable

# 	def __init__(self, name, email):
# 		self.name = name
# 		self.email = email
# 		Contact.all_contacts.append(self)



class Supplier(Contact):
	def order(self, order):
		print("If this were a real system we would send "
			"'{}' order to '{}'".format(order, self.name))


# Overriding
class Friend(Contact):
	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		super().__init__(name, email) # calling the original to avoid duplicates
		self.phone = phone # new

f = Friend('L', 'email', '555')
c = Contact('C', 'gmail')
print(Friend.all_contacts) # here is where the duplicates comes in
print(Contact.all_contacts) # here too because

# c = Contact("Some Body", "somebody@example.net")
# s = Supplier("Sup Plier", "supplier@example.net")

# print(c.name, c.email, s.name, s.email)
# # print(c.all_contacts)

# print(s.order("I need pliers"))


c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
names = [c.name for c in Contact.all_contacts.search('John')]
# print(names)





class LongNameDict(dict):
	def longest_key(self):
		longest = None
		for key in self:
			if not longest or len(key) > len(longest):
				longest = key
		return longest



longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'
x = longkeys.longest_key()
# print(x)