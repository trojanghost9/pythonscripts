import json
from pprint import pprint


def parser():
    """
    Currently reads the data.json file and prints it out in a way that is human readable
    :return:
    """
    # this should be updated to read from a provided file instead of being hard coded
    with open('data.json') as data_file:
        data = json.load(data_file)

    pprint(data)

if __name__ == "__main__":
    parser()
