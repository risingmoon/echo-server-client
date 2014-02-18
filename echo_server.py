import socket

buffsize = 256

if __name__ == "__main__":
	server_socket = socket.socket(
		socket.AF_INET,
		socket.SOCK_STREAM,
		socket.IPPROTO_TCP)

	server_socket.bind(('127.0.0.1',50000))
	server_socket.listen(1)

	conn, addr = server_socket.accept()
	done = False
	response = ''

	while not done:
		msg_part = conn.recv(buffsize)
		print msg_part
		if len(msg_part) < buffsize:
			done = True
			conn.sendall("message received")
			conn.shutdown(socket.SHUT_WR)
			conn.close()
