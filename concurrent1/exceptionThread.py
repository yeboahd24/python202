#!usr/bin/env/python3

from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import threading
import random
 
 
def isEven(n):
    print("\nChecking if {} is even".format(n))
    if type(n) != int:
        raise Exception("Value entered is not an integer")
    if n % 2 == 0:
        print("\n{} is even".format(n))
        return True
    else:
        print("\n{} is odd".format(n))
        return False

def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        task1 = executor.submit(isEven, (2))
        task2 = executor.submit(isEven, (3))
        task3 = executor.submit(isEven, ('t'))  # exeption is raise here

    for future in concurrent.futures.as_completed([task1, task2, task3]):
        print("Result of Task: {}".format(future.result()))
 
if __name__ == '__main__':
    main()
