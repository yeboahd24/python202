#!usr/bin/env/python3

class MacroCommand(object):
	"""A command that executes a list of commands"""

	def __init__(self, commands):
		self.commands = list(commands) 

	def __call__(self):
		for command in self.commands: 
			command()

t = range(10)
macro = MacroCommand(t)
print(macro.commands)
