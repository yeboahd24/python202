#!usr/bin/env/python3

# setdefault works similary like get

stocks = {"GOOG": (613.30, 625.86, 610.50), "MSFT": (30.25, 30.70, 30.19)}

# print(stocks.get("RIM")) # None
# print(stocks.get("RIM", "INVALID"))

stocks.setdefault("BBRY", (10.50, 10.62, 10.39))
# print(stocks['BBRY'])


# counting occurrence of words
def letter_frequency(sentence):
	frequencies = {}
	for letter in sentence:
		frequency = frequencies.setdefault(letter, 0)
	frequencies[letter] = frequency + 1
	return frequencies


# updated version

from collections import defaultdict
def letter_frequency(sentence):
	frequencies = defaultdict(int)
	for letter in sentence:
		frequencies[letter] += 1
	return frequencies


# new version
def letter_frequency(sentence):
	return Counter(sentence)



# this module helps in sorting base on certain criterails
import operator

inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]

group = operator.itemgetter(1)  # ('orange', 1) begins
x=sorted(inventory, key=group)
# print(x)



song_library = [("Phantom Of The Opera", "Sarah Brightman"),
 ("Knocking On Heaven's Door", "Guns N' Roses"),
 ("Captain Nemo", "Sarah Brightman"),
 ("Patterns In The Ivy", "Opeth"),
 ("November Rain", "Guns N' Roses"),
 ("Beautiful", "Sarah Brightman"),
 ("Mal's Song", "Vixy and Tony")]

artists = set()
for song, artist in song_library:
	artists.add(artist)
print(artists)