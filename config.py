from dataclasses import dataclass
import json

@dataclass
class Config:
    """Class used to structure config file.  
    Keys in JSON file needs to have this same names as class properities
    """
    some_key1: str
    some_key2: str

def load_config(file_path):
    """Function used to initialize Config with JSON data

    Args:
        file_path ([string]): path to JSON file

    Returns:
        dataclass: class with JSON keys as properities
    """    
    with open(file_path, "r") as config_file:
        config = json.load(config_file)
    return Config(**config)
