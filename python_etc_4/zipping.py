#!usr/bin/env/python3

# reading

# gzip compression
import gzip
with gzip.open('somefile.gz', 'rt') as f:
	text = f.read()

# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
	text = f.read()


# writing

# gzip compression
import gzip
with gzip.open('somefile.gz', 'wt') as f:
	f.write(text)
	
# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
	f.write(text)