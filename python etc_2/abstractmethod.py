# def human_name(self):
# 	raise NotImplementedError


from abc import ABCMeta, abstractmethod

class Service(metaclass=ABCMeta):
	'''Try to avoid NotImplementedError as your absractmethod
	because it has a downside. You get the error only upon
	method call not on class instiation.S'''


	@abstractmethod
	def human_name(self):
		pass



	





