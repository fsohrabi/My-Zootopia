FILE_PATH = "animals.html"


def write_data(data):
    with open(FILE_PATH, "w") as handel:
        handel.write(data)
