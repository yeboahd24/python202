#!usr/bin/env/python3
# the following class, which allows a user to fetch URLs using a kind
# of templating scheme.
from urllib.request import urlopen
class UrlTemplate:
	def __init__(self, template):
		self.template = template

	def open(self, **kwargs):
		return urlopen(self.template.format_map(kwargs))

# Example use. Download stock data from yahoo
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
	print(line.decode('utf-8'))

#with closure
def urltemplate(template):
	def opener(**kwargs):
		return urlopen(template.format_map(kwargs))
	return opene
# Example use
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
	print(line.decode('utf-8'))