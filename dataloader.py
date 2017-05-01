def load_data(path_file):
    file = open(path_file, 'r')
    doc = file.read()
    file.close()
    return doc