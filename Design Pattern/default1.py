#!usr/bin/env/python3

from queue import Queue, LifoQueue, PriorityQueue

#FIFO
lineup = Queue(maxsize=3)
# lineup.get(block=False)
# print(lineup) # error because is empty but setting block=True will not display the error

# lineup.put("one")
# lineup.put("two")
# lineup.put("three")
# lineup.put("four", timeout=0) # error because the size is set to 3
# print(lineup.get())  # this act like generators one thing at a time

#LIFO
stack = LifoQueue(maxsize=3)
stack.put("one")
stack.put("two")
stack.put("three")
# stack.put("four", block=False) # error
# print(stack.get()) # act like list


priority = PriorityQueue(maxsize=4)

priority.put((3, "three"))
priority.put((4, "four"))
priority.put((1, "one") )  
priority.put((2, "two"))
# priority.put((5, "five"), block=False) # error because is full

# print(priority.get())  # (1, 'one') because is the priority



