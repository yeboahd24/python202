#!usr/bin/env/python3


class Options:
	default_options = {
				'port': 21,
				'host': 'localhost',
				'username': None,
				'password': None,
				'debug': False,
			}


	def __init__(self, **kwargs):
		self.options = dict(Options.default_options)
		# self.options.update(kwargs)
		self.options |= kwargs # new version style

	def __getitem__(self, key):
		return self.options[key]


options = Options(username="dusty", password="drowssap", debug=True)  # debug is overide
print(options['debug'])
