from lettuce import step
from lettuce import world

import socket
from echo_server import socket_setup, recv

@step('client message string (.*)')
def client_nesssage_string(step,message):
    world.client_message = message

@step('I pass socket and buffer')
def pass_socket_and_buffer(step):
    world.server_socket = socket_setup()
    world.server_socket.bind(('127.0.0.1',50000))
    world.server_socket.listen(1)


    world.client_socket = socket_setup()
    world.client_socket.connect(('127.0.0.1',50000))
    world.client_socket.sendall(world.client_message)
    world.client_socket.shutdown(socket.SHUT_WR)

    world.conn, world.addr = world.server_socket.accept()
    world.response = recv(world.conn, 8)
    
@step('I see (.*)')
def compare(step,expected):
    assert  world.response == expected, 'response: %s' %world.response
    