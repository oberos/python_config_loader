from config import load_config


config2 = load_config("config.json")
print(config2.some_key1)
print(config2.some_key2)
