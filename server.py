import threading
from src import socketlib
from src import handlers


HOST = ''
PORT = 80
# CONFIG_PATH = '/etc/httpd.conf'
# HOST = '127.0.0.1'
# PORT = 6060
CONFIG_PATH = './src/httpd.conf'


def read_config_file():
    try:
        file = open(CONFIG_PATH, 'r')
    except FileNotFoundError:
        exit('Config file {} is not found'.format(CONFIG_PATH))

    file_data = file.read().split('\n')
    file.close()

    if not file_data:
        exit('No file data {}'.format(CONFIG_PATH))

    data_dict = {}
    for elem in file_data:
        if elem:
            elems = elem.split()
            data_dict[elems[0]] = elems[1]

    return data_dict


if __name__ == '__main__':
    listen_socket = socketlib.create_socket(HOST, PORT)
    print('Listening on {}'.format(listen_socket.getsockname()))

    config_data = read_config_file()
    thread_pool = []

    for i in range(int(config_data['thread_limit'])):
        thread = threading.Thread(target=handlers.handler_client,
                                  args=[listen_socket, config_data['document_root']],
                                  daemon=True)
        thread_pool.append(thread)
        thread.start()

    for thread in thread_pool:
        thread.join()
