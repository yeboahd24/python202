# x = 'AB'
# y = 'AB'
# # print(x==y)
# # print(x is y)


# a = [1,2]
# b = [1,2]
# print(a==b)
# print(a is b) #False


a = '1234'
b = '1235'
c = '1236'
y = int(max(a)) + int(max(b)) + int(max(c))
z = int(min(a)) + int(min(b)) + int(min(c))
rest = y-z

# print(rest)
import re
x =[str(i) for i in range(21)]
x = str(x)

p = re.findall(r'\d?\d*[2|0-]',x )
# print(p)
# x 1,2,12,22
# print(type(x))


class Seq:#protocol(duck typing, behaving like sequence)
	def __init__(self, seq):
		self.seq = list(seq)
	def __getitem__(self, index): # support iter too(partial protocol)
		return self.seq[index]

	def __len__(self):
		return len(self.seq)

	def __setitem__(self, pos, val):
		self.seq[pos]=val









x = [1,2,3,4,5]
s = Seq(x)
# print(s[1])
# print(len(s))
# for i in s:
# 	print(i)

# s[0]=0
# print(s[0])



def test(n):
	for i in n:
		yield i


def foo():
	yield from test(range(10))

n = [range(10)]
for i in foo():
	print(i)

