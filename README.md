# Python Config Loader

This snippet allow to load JSON file directly to python dataclass.

## Getting started

Requires at least Python 3.7.  
Put `config.py` and `config.json` files in your project.  
Fill `config.json` with your key: value pairs.  
Modify `Config` dataclass in `config.py` file to represent json keys  

# Usage

```python
from config import load_config


config2 = load_config("config.json")
print(config2.some_key1)
print(config2.some_key2)
```
