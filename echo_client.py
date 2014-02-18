import sys
import socket

buffsize = 256

if __name__ == "__main__":
	client_socket = socket.socket(
		socket.AF_INET,
		socket.SOCK_STREAM,
		socket.IPPROTO_IP)
	client_socket.connect(('127.0.0.1',50000))
	client_socket.sendall(sys.argv[1])
	client_socket.shutdown(socket.SHUT_WR)

	done = False
	response = ''

	while not done:
		msg_part = client_socket.recv(buffsize)
		print msg_part
		if len(msg_part) < buffsize:
			done = True
			client_socket.close()