#!usr/bin/env/python3
from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a, b)
print(len(c)) # 3

print(c['x']) # Outputs 1 (from a)  more pythonic
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

#similar sitution with update
b.update(a)
print(b['x'])
print(b['y'])
print(b['z'])

print(len(b)) # 3