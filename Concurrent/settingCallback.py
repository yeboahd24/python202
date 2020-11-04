#!usr/bin/env/python3

# Callback is used to notify when some work is completed

from concurrent.futures import ThreadPoolExecutor
import time

# def task(n):
#   print("Processing {}".format(n))

# def taskDone(fn):
#   if fn.cancelled():
#     print("Our {} Future has been cancelled".format(fn.arg))
#   elif fn.done():
#     print("Our Task has completed")

# def secondTaskDone(fn):
#   print("I didn't think this would work")

# def main():
#   print("Starting ThreadPoolExecutor")
#   with ThreadPoolExecutor(max_workers=3) as executor:
#     future = executor.submit(task, (2))
#     future.add_done_callback(taskDone)
#     future.add_done_callback(secondTaskDone)

    
#   print("All tasks complete")
    
# if __name__ == '__main__':
#   main()



def taskOne():
	print("Ok I'm waiting for your call")

	time.sleep(.3)

def workDone(n):
	print("I'm at home now")


def main():
	print("I'm at work now I will call you when I got home")

	with ThreadPoolExecutor(max_workers=3) as executor:
		future = executor.submit(taskOne)
		future.add_done_callback(workDone)

if __name__ == '__main__':
	main()