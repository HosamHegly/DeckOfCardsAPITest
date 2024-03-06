import json
from os.path import dirname, join


def get_filename(filename):
    here = dirname(__file__)
    output = join(here, filename)
    return output


def get_config_data():
    filename = get_filename("../config.json")
    with open(filename, 'r') as file:
        config = json.load(file)
        return config
