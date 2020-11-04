#!usr/bin/env/python3

# Note by default every class has this behaviors get, set, del

# Eg
class Generic:
	pass

g = Generic()
g.attribute = 1
# print(g.attribute)
# del g.attribute


# this also the same
from types import SimpleNamespace

n = SimpleNamespace()
n.simple = 1
# print(n.simple)
# del n.simple

