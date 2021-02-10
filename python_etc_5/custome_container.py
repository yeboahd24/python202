#!usr/bin/env/python3

import collections
import bisect


class SortedItems(collections.Sequence):
	def __init__(self, initial=None):
		self._items = sorted(initial) if initial is not None else []

	# Required sequence methods
	def __getitem__(self, index):
		return self._items[index]

	def __len__(self):
		return len(self._items)

	# Method for adding an item in the right location
	def add(self, item):
		bisect.insort(self._items, item)  # inward sorting


items = SortedItems([5, 1, 3])
# items.add(1)
# items.add(3)
# items.add(2)
print(list(items))