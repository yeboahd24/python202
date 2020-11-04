#!usr/bin/env/python3

import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

# values = [2,3,4,5,6,7,8]

# def multiplyByTwo(n):
#   return 2 * n

# def main():
#   with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(multiplyByTwo, values)
#     for result in results:
#       print(result)

# if __name__ == '__main__':
#   main()
  # results = list(map(multiplyByTwo, values))
  # print(results)



values = range(1, 21)

def multiplyByTwo(n):
	answers = 2 * n
	return(f'\n{2} * {n} = {answers}')

def main():
	with ThreadPoolExecutor(max_workers=3) as executor:
		results = executor.map(multiplyByTwo, values)
		for result in results:
			print(result)
if __name__ == '__main__':
	main()