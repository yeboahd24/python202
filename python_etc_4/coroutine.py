#!usr//bin/env/python3

def simple_coroutine(): #
	print('-> coroutine started')
	x = yield # to recive data from the client
	print('-> coroutine received:', x)


my_coro = simple_coroutine()
print(my_coro) # coroutine/generator
print(next(my_coro)) # starting coroutine
print(my_coro.send(42))  # coroutine recieve: 42

