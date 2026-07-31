#!/usr/bin/python3
"""Module that defines a function to save an object as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a text file.

    Args:
        my_obj: The object to serialize. Must be JSON serializable.
        filename (str): The path of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
