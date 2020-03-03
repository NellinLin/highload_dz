import threading
from src import socketlib
from src import handlers
from src.readconf import read_config_file


HOST = ''
PORT = 80
CONFIG_PATH = '/etc/httpd.conf'
# HOST = '127.0.0.1'
# PORT = 6060
# CONFIG_PATH = './src/httpd.conf'


if __name__ == '__main__':
    listen_socket = socketlib.create_socket(HOST, PORT)
    print('Listening on {}'.format(listen_socket.getsockname()))

    config_data = read_config_file(CONFIG_PATH)
    thread_pool = []

    for i in range(int(config_data['thread_limit'])):
        thread = threading.Thread(target=handlers.handler_client,
                                  args=[listen_socket, config_data['document_root']],
                                  daemon=True)
        thread_pool.append(thread)
        thread.start()
        thread.join()
