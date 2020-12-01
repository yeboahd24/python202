#!usr/bin/env/python3


# class InvalidWithdrawal(Exception):
# 	pass
# raise InvalidWithdrawal("You don't have $50 in your account")



# Exception with arguments



class InvalidWithdrawal(Exception):
	def __init__(self, balance, amount):
		super().__init__("account doesn't have ${}".format(amount))
		self.amount = amount
		self.balance = balance

	def overage(self):
		return self.amount - self.balance
# raise InvalidWithdrawal(25, 50)



# try:
# 	raise InvalidWithdrawal(25, 50)
# except InvalidWithdrawal as e:
# 	print("I'm sorry, but your withdrawal is "
# "more than your balance by "
# "${}".format(e.overage()))



class ATM(object):
	def __init__(self, amount, balance):
		self.amount = amount
		self.balance = balance

	def check_balance(self):
		try:
			raise InvalidWithdrawal(self.amount, self.balance)
			
		except InvalidWithdrawal as e:
			return e.overage()


atm = ATM(200, 100)
print(atm.check_balance())







