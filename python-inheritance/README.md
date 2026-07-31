# python-inheritance

Higher-level programming project on inheritance in Python 3.

## Tasks

| File | Description |
| --- | --- |
| `0-lookup.py` | List an object's attributes and methods |
| `1-my_list.py` | A `list` subclass that can print itself sorted |
| `2-is_same_class.py` | Check exact class membership |
| `3-is_kind_of_class.py` | Check class membership including subclasses |
| `4-inherits_from.py` | Check strict (non-exact) class heritage |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with an unimplemented `area()` |
| `7-base_geometry.py` | `BaseGeometry` with `integer_validator` |
| `8-rectangle.py` | `Rectangle`, validated width/height, no `area()` yet |
| `9-rectangle.py` | `Rectangle` with `area()` and `__str__` |
| `10-square.py` | `Square` built on `Rectangle`, no `__str__` override |
| `11-square.py` | `Square` with its own `__str__` |

Doctest files for tasks 1 and 7 live in `tests/` and run with:

```
python3 -m doctest ./tests/*
```

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- pycodestyle 2.7.*
- All modules, classes and functions are documented
- All files start with `#!/usr/bin/python3` and are executable
