#!usr/bin/env/python3

# Inheriting from Enum makes your class immutable
from enum import Enum

class Suit(Enum):
	Club = '1'
	Diamond = '2'
	Heart = '3'
	Spade = '4'

# print(Suit.Club.value)
# Suit.Club.value = '2'
