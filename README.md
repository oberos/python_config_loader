# Python Config Loader

This snippet allow to load JSON file directly to pydantic model.

## Getting started

Requires [Pydantic](https://pydantic-docs.helpmanual.io).  
Put `config` folder in your project.  
Modify `Main` model in `config.py` according to your needs  
Run `config.py` file to generate `config.json` template  
Fill `config.json` with your key: value pairs.  

# Usage
```JSON
{
    "some_key1": "some_value1",
    "some_key2": "some_value2",
    "some_key3": [1, 2, 3],
    "some_key4": {
        "sub_key1": "some_sub_value1",
        "sub_key2": "some_sub_value2"
    },
    "some_key5": ""
}
```

```python
from config import load_config


config = load_config()
print(config)
print(config.some_key1)
print(config.some_key2)
print(config.some_key3)
print(config.some_key4)
print(config.some_key4.sub_key1)
```

Outputs
```
some_key1='some_value1' some_key2='some_value2' some_key3=[1, 2, 3] some_key4=Sub(sub_key1='some_sub_value1', sub_key2='some_sub_value2')
some_value1
some_value2
[1, 2, 3]
sub_key1='some_sub_value1' sub_key2='some_sub_value2'
some_sub_value1
```
