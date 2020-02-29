from src import socketlib


def handler_client(listen_socket, document_root):
    while True:
        client_socket, client_address = listen_socket.accept()

        try:
            message = socketlib.receive_message(client_socket)
            message = '{}: {}'.format(client_address, message)
            print(message)
            # socketlib.send_message(client_socket, message)
        except (ConnectionError, BrokenPipeError):
            print('Socket error')
        finally:
            print('Closed connection to {}'.format(client_address))
            client_socket.close()
