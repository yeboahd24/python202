#!usr/bin/env/python3

# concatenating bytes and str objects

# test1 = b'abc' + 'def'
# print(test1) # wrong

# God way
test2 = b'abc'.decode('latin1') + 'def'
print(test2)
test3 = b'abc' + 'def'.encode('latin1')
print(test3)
