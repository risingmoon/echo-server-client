import socket



def socket_setup():
	"""Returns and setup a socket based on this
	project's configuration"""
	return socket.socket(
		socket.AF_INET,
		socket.SOCK_STREAM,
		socket.IPPROTO_TCP)

def recv(connection, buffer_size):

	response = ''
	done = False
	while not done:
		msg_part = connection.recv(buffer_size)
		response += msg_part
		if len(msg_part) < buffer_size:
			done = True
	return response

if __name__ == "__main__":
	#Setup server socket with socket_setup()
	server_socket = socket_setup()

	#Bind and set server socket to listen
	server_socket.bind(('127.0.0.1',50000))
	server_socket.listen(1)

	connection, address = server_socket.accept()

	response = recv(connection,8)

	connection.sendall("message received")
	connection.shutdown(socket.SHUT_WR)
	connection.close()

	print response

