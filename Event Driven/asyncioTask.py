#!usr/bin/env/python3


import asyncio

async def myCoroutine():
  print("My Coroutine")

async def main():
  await asyncio.sleep(1)

loop = asyncio.get_event_loop()
try:
  loop.create_task(myCoroutine())  # this helps to create many tasks with one thread
  loop.create_task(myCoroutine())	
  loop.create_task(myCoroutine())

  pending = asyncio.all_tasks(loop=loop)
  print(pending)
  loop.run_until_complete(main())
finally:
  loop.close()
