#!usr/bin/env/python3

# Charging system

import threading
from time import sleep

state = threading.Semaphore(value=1)  # initial value is always 1
# state = threading.BoundedSemaphore(1) # same as the Semaphore but this prevent programatic errors

def cell_phones():
	name = threading.current_thread().getName()
	with state:  # using context manager here
		print('Phone is charging...')
		sleep(2)
		print('Done charging')

if __name__ == '__main__':
	for phone in range(10):
		threading.Thread( target=cell_phones, name="phones-" +str(phone)).start()