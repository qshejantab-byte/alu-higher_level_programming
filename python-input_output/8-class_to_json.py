#!/usr/bin/python3
"""Module that defines a function to describe an object for JSON use."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON use.

    Args:
        obj: An instance whose attributes are all serializable
            (list, dictionary, string, integer, boolean).

    Returns:
        dict: A dictionary of the object's attributes.
    """
    return obj.__dict__
