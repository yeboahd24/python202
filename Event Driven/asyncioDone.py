#!usr/bin/env/python3
import asyncio

async def show():
	print("I'm at the church I will call you when I'm closed")
	await asyncio.sleep(.3)

def notify(n):
	print("I'm done, Calling...")


def main():
	loop = asyncio.get_event_loop()
	task = loop.create_task(show())
	task.add_done_callback(notify)
	loop.run_until_complete(task)

if __name__=="__main__":
	main()

