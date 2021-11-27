from config import load_config


config = load_config()
print(config)
print(config.some_key1)
print(config.some_key2)
print(config.some_key3)
print(config.some_key4)
print(config.some_key4.sub_key1)
