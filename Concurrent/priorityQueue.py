#!usr/bin/env/python3

# Priority Queue is like VVIP

import threading
import queue
import random
import time

def mySubscriber(queue):
  while not queue.empty():
    item = queue.get()
    if item is None:
      break
    print("{} removed {} from the queue".format(threading.current_thread(), item))
    queue.task_done()
    time.sleep(1)


myQueue = queue.PriorityQueue()

for i in range(5):
  myQueue.put(i, i)  # (0, 0) is the priority

for i in range(5):
  myQueue.put(i, i)  # same as here

print("Queue Populated")

threads = []
for i in range(2):
  thread = threading.Thread(target=mySubscriber, args=(myQueue,))
  thread.start()
  threads.append(thread)

for thread in threads:
  thread.join()

print("Queue is empty")
