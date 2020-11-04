#!usr/bin/env/python3


import asyncio

async def myCoroutine():
	print("My Coroutine")

async def main():
	current = asyncio.current_task()
	print(current)

loop = asyncio.get_event_loop()
try:
	task1 = loop.create_task(myCoroutine())
	task2 = loop.create_task(myCoroutine())
	task3 = loop.create_task(myCoroutine())  # task3 is cancelled
	task3.cancel()
	loop.run_until_complete(main())
finally:
	loop.close()