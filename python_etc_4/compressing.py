#!usr/bin/env/python3
from itertools import compress
# itertools.compress() takes an iterable and
# an accompanying Boolean selector sequence as input. 

addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK'
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
# Now suppose you want to make a list of all addresses where the corresponding count
# value was greater than 5. Here’s how you could do it
more5 = [n > 5 for n in counts]
print(more5)  # boolean
print(list(compress(addresses, more5)))
