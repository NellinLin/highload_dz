import socket


def create_socket(host, port):
    new_socket = socket.socket()
    new_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_socket.bind((host, port))
    new_socket.listen(100)
    return new_socket
