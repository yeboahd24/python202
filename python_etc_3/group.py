#!usr/bin/env/python3

rows = [
 {'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))


# Iterate in groups

#An important preliminary step is sorting the data according
#to the field of interest. Since
# groupby() only examines consecutive items, failing to sort first won’t group the records
# as you want.
for date, items in groupby(rows, key=itemgetter('date')):
	print(date)
	for i in items:
		print(' ', i)
