import json

__name = ""
__port = ""
__baudrate = ""
__new_line = ""

def restore_config():
    global __name, __port, __baudrate, __new_line
    LUT = __get_names_LUT()
    restore_file_handler = open("restore.ini", "r")
    config_name = restore_file_handler.readline().strip()
    restore_file_handler.close()
    config_file_handler = open("config.json", "r")
    config = json.load(config_file_handler)
    config_file_handler.close()
    config = config["config"]
    config = config[LUT[config_name]]
    __name = config["name"]
    __port = config["port"]
    __baudrate = config["baudrate"]
    __new_line = config["new_line"]

def __get_names_LUT():
    LUT = {}
    config_dict_list = get_avalible_configs()
    for index, dict in enumerate(config_dict_list):
        LUT[dict["name"]] = index
    return LUT

def get_name():
    global __name
    return __name

def get_port():
    global __port
    return __port

def get_baudrate():
    global __baudrate
    return __baudrate

def get_new_line():
    global __new_line
    return __new_line

def get_avalible_configs():
    config_file_handler = open("config.json", "r")
    config = json.load(config_file_handler)
    config_file_handler.close()
    config = config["config"]
    return config

def select_config(name):
    global __name, __port, __baudrate, __new_line
    LUT = __get_names_LUT()
    available_config_names = LUT.keys()
    if name not in available_config_names:
        raise Exception("Config Key Error.")
    restore_file_handler = open("restore.ini", "w")
    restore_file_handler.write(name)
    restore_file_handler.close()
    config_file_handler = open("config.json", "r")
    config = json.load(config_file_handler)
    config_file_handler.close()
    config = config["config"]
    config = config[LUT[name]]
    __name = config["name"]
    __port = config["port"]
    __baudrate = config["baudrate"]
    __new_line = config["new_line"]

def to_string_current_config():
    return __name + "\n" + __port + "\n" + str(__baudrate) + "\n" + __new_line + "\n"

def to_string_config():
    name = ""
    port = ""
    baudrate = ""
    new_line = ""
    string = ""
    configs = get_avalible_configs()
    for config in configs:
        name = config["name"]
        port = config["port"]
        baudrate = str(config["baudrate"])
        new_line = config["new_line"]
        string += name + "\n" + port + "\n" + str(baudrate) + "\n" + new_line + "\n-----------------\n\n"
    return string
