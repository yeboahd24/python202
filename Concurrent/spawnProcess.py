#!usr/bin/env/python3

# getting PID of each sub-process helps in logging and debugging


import multiprocessing
import time

def childTask():
    print("Child Process With PID: {}".format(multiprocessing.current_process().pid))
    time.sleep(3)
    print("Child process terminating")

def main():
    print("Main process PID: {}".format(multiprocessing.current_process().pid))
    myProcess = multiprocessing.Process(target=childTask)
    myProcess.start()
    myProcess.join()

if __name__ == '__main__':
    main()
