#!usr/bin/env/python3

# using abstract class force the subclass

from abc import ABCMeta, abstractmethod
class AbstractBettingStrategy(metaclass=ABCMeta):

	@abstractmethod
	def bet(self) -> int:
		pass

	@abstractmethod
	def record_win(self) -> None:
		pass

	@abstractmethod
	def record_loss(self) -> None:
		pass


class Simple_Broken(AbstractBettingStrategy):
	def bet( self ):
		return 1

# simple = Simple_Broken()
# print(simple)  # error because all methods is not implemented

