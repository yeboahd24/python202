#!usr/bin/env/python3

#character matching with wildcards

addresses = [
 '5412 N CLARK ST',
 '1060 W ADDISON ST',
 '1039 W GRANVILLE AVE',
 '2122 N CLARK ST',
 '4802 N BROADWAY',
]

x = [i for i in addresses if i.endswith('ST')]
print(x)

#alternatively
from fnmatch import fnmatchcase
y = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(y)