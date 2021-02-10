#!usr/bin/env/python3
from contextlib import suppress

# Normall Exception
try:
    lst = [1, 2, 3, 4, 5]
    print(lst[10]) # getting index that does't exist
except IndexError:
    print('Index Error')

#Elegant way
# with suppress(IndexError):
#     lst = [1,2,3,4,5]
#     lst[10]