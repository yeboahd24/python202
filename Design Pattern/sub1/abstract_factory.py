#!usr/bin/env/python3
from decimal import Decimal

class Factory(object):  # acting like abstract method

        def build_sequence(self):  
            return []

        def build_number(self, string):
            return Decimal(string)



class Loader(object):
        def load(string, factory):  # note this does not take self
            sequence = factory.build_sequence() # list
            for substring in string.split(','):
                item = factory.build_number(substring)
                sequence.append(item)
            return sequence

f = Factory()
result = Loader.load('1.23, 4.56', f)
print(result)
