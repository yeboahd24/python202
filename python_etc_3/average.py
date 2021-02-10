#!usr/bin/env/python3

class Averager():

	def __init__(self):
		self.series = []

	def __call__(self, new_value):
		self.series.append(new_value)
		total = sum(self.series)
		return total/len(self.series)


avg = Averager()
print(avg(10))

#closure
def make_averager():
	series = []

	def averager(new_value):
		series.append(new_value)
		total = sum(series)
		return total/len(series)
	return averager

# calling make_averger() returns averager()
av = make_averager()  #calling make_averager(10) give error
print(av(10))




# def make_averager():
# 	count = 0
# 	total = 0

# 	def averager(new_value): # error because count and total are immutable
# 		count += 1
# 		total += new_value
# 		return total / count
# 	return averager





def make_averager():
	count = 0
	total = 0

	def averager(new_value):
		nonlocal count, total
		count += 1
		total += new_value
		return total / count
	return averager


a = make_averager()
print(a(10))