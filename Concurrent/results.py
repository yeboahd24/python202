#!usr/bin/env/python3

# using done() method 


import time
import random
from concurrent.futures import ThreadPoolExecutor


values = [2,3,4,5,6,7,8]

def multiplyByTwo(n):
  time.sleep(random.randint(1,2))
  return 2 * n

def done(n):
  print("Done: {}".format(n))

def main():
  with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(multiplyByTwo, values)

    for result in results:
      done(result)  #note instead of using print() we use done here to mean the same

if __name__ == '__main__':
  main()