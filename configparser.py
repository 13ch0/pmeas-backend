import json

def read_config_file():
    """
    Reads the configuration file stored in config/
    Returns string being read.
    """
    config_file = open("config/effects.txt")
    config_data = config_file.read()
    config_file.close()
    return config_data

def parse_config_file(config_data):
    """
    Parse the data from the file into respective
    objects.
    Currently prints the objects to the screen for testing.
    """
    config_data = json.loads(config_data)
    return config_data

def get_effects():
    file_contents = read_config_file()
    return parse_config_file(file_contents)
