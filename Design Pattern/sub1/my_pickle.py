#!usr/bin/env/python3

import pickle
#The dumps and loads functions behave much like their file-like counterparts, except
#they return or accept bytes instead of file-like objects. 
# use this  pickle.dumps(my_object, protocol=2) only if you want it to run in older versions.
some_data = ["a list", "containing", 5,
 "values including another list",
 ["inner", "list"]]

with open("pickled_list", 'wb') as file:
	pickle.dump(some_data, file)

with open("pickled_list", 'rb') as file:
	loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == some_data
