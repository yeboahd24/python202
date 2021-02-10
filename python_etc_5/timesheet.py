#!usr/bin/env/python
import re


pat_1 = re.compile(r'\d{1}-\d{1}') 
pat_2 = re.compile(r'\d{2}-\d{2}') 

with open("january.txt") as text:
	reader = text.read()

	# if re.findall(pat_1, reader):
	# 	print('START END ELAPSED')
	# 	print(f"{reader[0]:<5s} {reader[2]:6>s}")

	print(reader)



		


