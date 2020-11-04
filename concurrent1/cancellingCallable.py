#!usr/bin/env/python3

import time
import random
from concurrent.futures import ThreadPoolExecutor

def someTask(n):
  print("\nExecuting Task {}".format(n))
  time.sleep(n)
  print("\nTask {} Finished Executing".format(n))

def main():
  with ThreadPoolExecutor(max_workers=2) as executor:
    task1 = executor.submit(someTask, (1))
    task2 = executor.submit(someTask, (2)) # True
    task3 = executor.submit(someTask, (3))
    task4 = executor.submit(someTask, (4))

    print(task3.cancel())
  
if __name__ == '__main__':
  main()
