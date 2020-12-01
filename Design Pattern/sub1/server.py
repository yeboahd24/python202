#!usr/bin/env/python3


#The decorator pattern allows us to "wrap" an object that provides core functionality
#with other objects that alter this functionality.

#There are two primary uses of the decorator pattern:
	#• Enhancing the response of a component as it sends data to a second component
	#• Supporting multiple optional behaviors


import socket

def respond(client):
	response = input("Enter a value: ")
	client.send(bytes(response, 'utf8'))
	client.close()

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('localhost',2401))
	server.listen(1)

	try:
 		while True:
 			client, addr = server.accept()
 			respond(client)

	finally:
		server.close()