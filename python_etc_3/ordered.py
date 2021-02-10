#!usr/bin/env/python3

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
	print(key, d[key])


import json
x = json.dumps(d)  #'{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'
print(x)