#!usr/bin/env/python3


def tally():
	score = 0
	while True:
		increment = yield  score  # coroutine
		score+=increment


# first = tally()
# print(next(first)) # 0
# first.send(1)
# print(next(first))



def generator2():
    for i in range(10):  
        yield i

def generator3():
    for j in range(10, 20):
        yield j

def generator():
    for i in generator2():
        yield i
    for j in generator3():
        yield j




# Update with yield from 
# Before you use yield from the function must be iterated

def generator():
    yield from generator2()
    yield from generator3()

# n = generator()
# print(next(n))
# print(next(n))




