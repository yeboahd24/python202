#!usr/bin/env/python3

# import request

# class WebPage:
# 	def __init__(self, url):
#  		self.url = url
#  		self._content = None


#  	@property
#  	def content(self):
#  		if not self._content:
#  			print("Retrieving New Page")
#  			self._content = request.get(self.url).read()

#  		return self._content




class AverageList(list):

    @property
    def average(self):
    	return sum(self) / len(self)



avg = AverageList([1,2,3,4])
print(avg.average)