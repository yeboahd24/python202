#!usr/bin/env/python3
import re

#simple replace
text = 'yeah, but no, but yeah, but no, but yeah'
rep = text.replace('yeah', 'yep')
# print(rep)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

rep = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
# print(rep)

x = [1,2]
y = [2,1]
print(x==y)
print(set(x)==set(y))