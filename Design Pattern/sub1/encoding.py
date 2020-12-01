#!usr/bin/env/python3
import sys
#Note we encode str and decode byte
characters = "cliché"
print(characters.encode("UTF-8"))
print(characters.encode("latin-1"))
print(characters.encode("CP437"))

print(sys.getdefaultencoding())