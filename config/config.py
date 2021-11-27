
from pydantic import BaseModel


class Sub(BaseModel):
    sub_key1: str
    sub_key2: str

class Main(BaseModel):
    some_key1: str
    some_key2: str
    some_key3: list
    some_key4: Sub


def load_config():
    return Main.parse_file("config/config.json")
