#!usr/bin/env/python3

from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper') # same as s.upper()
print(upcase(s))
hiphenate = methodcaller('replace', ' ', '-')  # same as s.replace(' '. '-')
print(hiphenate(s))

index = methodcaller('index', 'T')
print(index(s))