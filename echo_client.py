import sys
import socket
from echo_server import socket_setup, recv


if __name__ == "__main__":
	
	client_socket = socket_setup()

	client_socket.connect(('127.0.0.1',50000))
	client_socket.sendall(sys.argv[1])
	client_socket.shutdown(socket.SHUT_WR)

	response = recv(client_socket, 8)
	print response