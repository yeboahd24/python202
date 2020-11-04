#!usr/bin/env/python3

# we use slot to limit memory space

class BlackJackCard:
	__slots__ = ("rank", "suit", "hard", "soft") # this avoid adding axtra

	def __init__(self, rank: str, suit: "suit", hard: int, soft: int) -> None:
		self.rank = rank
		self.suit = suit
		self.hard = hard
		self.soft = soft

