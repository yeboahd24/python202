#!usr/bin/env/python3


import io
import tokenize
code = io.StringIO("""
... if __name__ == "__main__":
... print("hello world!")
... """)
tokens = tokenize.generate_tokens(code.readline)
for token in tokens:
	print(token)