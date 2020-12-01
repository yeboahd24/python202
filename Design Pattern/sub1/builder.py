#!usr/bin/env/python3

from typing import NamedTuple
# Real Python code takes advantage of optional arguments
# to specify whatever combination of attributes it wants:



class Port(NamedTuple):
   number: int
   name: str = ''
   protocol: str = ''


Port(2)
Port(7, 'echo')
Port(69, 'tftp', 'UDP')


# Keyword arguments even let you skip earlier arguments:

port = Port(517, protocol='UDP')
# print(port)

# But what if Python lacked optional arguments?
# Then we might engage in contortions like:

class PortBuilder(object):
   def __init__(self, port): # awlays takes attribute as of the target
       self.port = port
       self.name = None
       self.protocol = None

   def build(self):
       return Port(self.port, self.name, self.protocol)



# The Builder lets the caller create a Port without
# needing to specify a value for every attribute.
# Here we skip providing a “name”:

b = PortBuilder(517)
b.protocol = 'UDP'
print(b.build())
