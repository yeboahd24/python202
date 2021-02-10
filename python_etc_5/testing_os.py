#!usr/bin/env/python3

import os
from datetime import datetime

# print(os.getcwd()) # current working directory

# os.chdir('D:\Python201\python etc') # changing directory
# print(os.listdir()) # getting files in the directory
# os.mkdir("python_etc_6") # making directory/not top levels
# print(os.listdir())
# os.makedirs("Demo/python_etc_6") # dirctory with top level folder

#removing dir
# os.rmd()
# os.removedirs()

# os.rename('os_test.txt', 'os.txt') # renaming file
# print(os.stat('os.txt')) # getting info about the file
# mode = os.stat('os.txt').st_mtime
# print(datetime.fromtimestamp(mode)) # more readable now

# for dirpath, dirnames, filenames in  os.walk(os.getcwd()): # Top Level
# 	print(f"Current Path: {dirpath}")
# 	print(f"Directory: {dirnames}")
# 	print(f"Files: {filenames}")
# 	print()
	
