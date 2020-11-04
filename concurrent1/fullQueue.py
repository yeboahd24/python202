#!usr/bin/env/python3

# limiting the size of our queue

import threading
import queue
import time

def myPublisher(queue):
  while not queue.full():
    queue.put(1)
    print("{} Appended 1 to queue: {}".format(threading.current_thread(), queue.qsize()))
    time.sleep(1)

myQueue = queue.Queue(maxsize=5)
# for i in range(10):
#   myQueue.put(i)

threads = []
for i in range(8): # only 5 item will be populated
  thread = threading.Thread(target=myPublisher, args=(myQueue,))
  thread.start()
  threads.append(thread)
for i in threads:
 	i.join()

