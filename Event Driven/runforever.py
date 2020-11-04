#!usr/bin/env/python3


import asyncio

def main():
  print("Creating our event loop")  # This will run forever until you stop it.
  loop = asyncio.get_event_loop()
  
  loop.run_forever()
  print("Our Loop will now run forever, this will never execute")

if __name__ == '__main__':
  main()