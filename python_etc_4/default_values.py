#!usr/bin/evn/python3
# If the default value is supposed to be a mutable container, such as a list, set, or dictionary,
# use None as the default and write code like this:

# Using a list as a default value
def spam(a, b=None):
	if b is None:
		b = []
		b.append(a)   #OUT: [0][1][2]...
	return b

# for i in range(10):
# 	print(spam(i))

#Bad way
def spam_1(a, b=[]):
	b.append(a)
	return b
	
for i in range(10):
	print(spam_1(i))               
#OUT:
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




