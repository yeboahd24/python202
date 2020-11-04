#!usr/bin/env/python3

"""	Daemon threads are 'essentially' threads that have no defined endpoint. They will continue
	to run forever until your program quits.
"""

import threading
import time

def standardThread():
    print("Starting my Standard Thread")
    time.sleep(20)
    print("Ending my standard thread")

def daemonThread():
    while True:
      print("Sending Out Heartbeat Signal")
      time.sleep(2)

if __name__ == '__main__':
	standardThread = threading.Thread(target=standardThread)
	daemonThread = threading.Thread(target=daemonThread)
	daemonThread.setDaemon(True)
	daemonThread.start()
  
	standardThread.start()


