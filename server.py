from src import socketlib

HOST = '127.0.0.1'
PORT = 6060

if __name__ == '__main__':
    listen_socket = socketlib.create_socket(HOST, PORT)
    print('Listening on {}'.format(listen_socket.getsockname()))

    while True:
        client_socket, client_address = listen_socket.accept()
