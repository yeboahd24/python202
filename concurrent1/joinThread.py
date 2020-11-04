#!usr/bin/env/python3

# join helps our program to be in order

import threading
import time

def ourThread(i):
  print("Thread {} Started".format(i))
  time.sleep(i*2)
  print("Thread {} Finished".format(i))

def main():
  thread = threading.Thread(target=ourThread, args=(1,))
  thread.start()
  # thread.join()  # if you join here you mean must finished without allowing thread2 to start

  print("\nIs thread 1 Finished?")

  thread2 = threading.Thread(target=ourThread, args=(2,))
  thread2.start()
  thread2.join()

  print("Thread 2 definitely finished")

if __name__ == '__main__':
  main()