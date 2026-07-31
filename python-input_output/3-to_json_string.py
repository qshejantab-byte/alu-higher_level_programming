#!/usr/bin/python3
"""Module that defines a function to serialize an object to JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj: The object to serialize. Must be JSON serializable.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
