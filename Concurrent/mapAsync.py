#!usr/bin/env/python3

# this can also be done with "map" but this is not a good way.

from multiprocessing import Pool
import time
def myTask(n):
	time.sleep(n/2)
	return n*2

def main():
	with Pool(4) as p:
		print(p.map_async(myTask, [4,3,2,1]).get())

if __name__ == '__main__':
 main()