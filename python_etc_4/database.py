#!usr/bin/env/python3

import sqlite3

#data
stocks = [
 ('GOOG', 100, 490.1),
 ('AAPL', 50, 545.75),
 ('FB', 150, 7.45),
 ('HPQ', 75, 33.2),
]

db = sqlite3.connect('database.db') # database name
c = db.cursor() # without this we can't execute
#NB: once table is created comment it because running it again will course an error
# c.execute('create table portfolio (symbol text, shares integer, price real)') # tabel 

c.executemany('insert into portfolio values (?,?,?)', stocks) #inserting
db.commit() # saving to the db

# for row in db.execute('select * from portfolio'):  # running it many times create duplicate
# 	print(set(row))


min_price = 100
for row in db.execute('select * from portfolio where price >= ?',(min_price,)):
	print(row)