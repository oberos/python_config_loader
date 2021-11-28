import json
from typing import List
from pydantic import BaseModel


class Sub(BaseModel):
    sub_key1: str = ""
    sub_key2: str = ""


class Main(BaseModel):
    some_key1: str = ""
    some_key2: str = ""
    some_key3: List = []
    some_key4: Sub = Sub()


def load_config():
    return Main.parse_file("config/config.json")


def save_template():
    print("saving template JSON to config.json")
    template = Main()
    with open("config.json", 'w') as data_file:
        data_file.write(json.dumps(template.dict(), indent=4))


if __name__ == '__main__':
    save_template()
