import configparser

CONFIG_PATH = 'config.ini'

def init():
    config_parser = configparser.ConfigParser()

    config_parser.read(CONFIG_PATH)
    
    return config_parser.get(section='Tokens', option='tokens', fallback=None)