from configparser import ConfigParser

def readConfig(key_header,key_value):
    config = ConfigParser()
    config.read("..\\Config\\config.ini")
    return config.get(key_header,key_value)




