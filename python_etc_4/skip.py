#!usr/bin/env/python3

from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]

for x in islice(items, 3, None): #skip first three values
	print(x)

#out: 1,4,10,15

# In this example, the last None argument to islice() is required to indicate that you
# want everything beyond the first three items as opposed to only the first three items
# (e.g., a slice of [3:] as opposed to a slice of [:3]).
















from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
# for x in chain(a, b):
# 	print(x)

#similar
# for i in a:
# 	print(i)
# for x in b:
# 	print(x)

#inefficient
for i in a+b:
	print(i)







# data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
# # Correct!
# for n, (x, y) in enumerate(data):
# 	print(n,x,y)