from src import socketlib


def handler_client(listen_socket, document_root):
    while True:
        client_socket, client_address = listen_socket.accept()

        try:
            request = socketlib.receive_message(client_socket)
            print('{}: {}'.format(client_address, request))
            response = socketlib.response_message(request, document_root)
            print(response)
            client_socket.sendall(response)
            client_socket.close()
        except (ConnectionError, BrokenPipeError):
            print('Socket error')
        finally:
            print('Closed connection to {}'.format(client_address))
            client_socket.close()
