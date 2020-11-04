#!usr/bin/env/python3


import asyncio
import time
# @asyncio.coroutine
async def myTask(n):
	time.sleep(1)
	print("Processing {}".format(n))

# @asyncio.coroutine
async def myGenerator():
	for i in range(5):
		asyncio.ensure_future(myTask(i))
	print("Completed Tasks")
	# yield from asyncio.sleep(2)
	await asyncio.sleep(2)


def main():
	loop = asyncio.get_event_loop()
	loop.run_until_complete(myGenerator())
	loop.close()

if __name__ == '__main__':
	main()

