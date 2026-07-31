#!/usr/bin/python3
"""Module that defines a function to load an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from the JSON content of a file.

    Args:
        filename (str): The path of the file to read from.

    Returns:
        The Python data structure represented by the file's content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
