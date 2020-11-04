#!usr/bin/env/python3

# Forking is process of cloning a given process
# PID = PROCESS IDENTIFIER

import os 

def child(): 
  print("We are in the child process with PID= %d"%os.getpid()) 
  
def parent(): 
  print("We are in the parent process with PID= %d"%os.getpid())
  newRef=os.getpid()  # try os.fork() because this don't work in python 3.9 now for me
  if newRef==0: 
    child() 
  else: 
    print("We are in the parent process and our child process has PID= %d"%newRef)
    
parent()

