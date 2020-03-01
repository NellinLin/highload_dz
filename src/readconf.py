def read_config_file(config_path):
    try:
        file = open(config_path, 'r')
    except FileNotFoundError:
        exit('Config file {} is not found'.format(config_path))

    file_data = file.read().split('\n')
    file.close()

    if not file_data:
        exit('No file data {}'.format(config_path))

    data_dict = {}
    for elem in file_data:
        if elem:
            elems = elem.split()
            data_dict[elems[0]] = elems[1]

    return data_dict
