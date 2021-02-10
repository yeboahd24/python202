#!usr/bin/env/python3

# The split() method of string objects is really meant for very simple cases, and does
# not allow for multiple delimiters or account for possible whitespace around the delim‐
# iters. In cases when you need a bit more flexibility, use the re.split() method:


line = 'asdf fjdk; afed, fjek,asdf, foo'

# print(line.split(';')) # does not allow multiple delimeters

import re

multiple_delimeters = re.split(r'[;,\s]\s*', line) # multiple delimeters
print(multiple_delimeters)

['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

