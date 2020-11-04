#!usr/bin/env/python3

#using send with generator


def psychologist():
	"""The send() send value to awiatable generator is like the next() """
	print('Please tell me your problems')
	while True:
		answer = (yield)  # this will pass through send
		if answer is not None:
			if answer.endswith('?'):
				print("Don't ask yourself too much questions")
			elif 'good' in answer:
				print("Ahh that's good, go on")
			elif 'bad' in answer:
				print("Don't be so negative")


# free = psychologist()
# print(next(free))
# free.send('I feel bad')
# print(next(free))
# free.send("Why I shouldn't ?")
# print(next(free))
# free.send("ok then i should find what is good for me")
# print(next(free))


