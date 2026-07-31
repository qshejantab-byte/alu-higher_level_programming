#!/usr/bin/python3
"""Module that defines a function to check strict class heritage."""


def inherits_from(obj, a_class):
    """Check whether an object is an instance of a strict subclass.

    Args:
        obj: The object to check.
        a_class: The ancestor class to compare against.

    Returns:
        bool: True if obj is an instance of a class that is a
            subclass of a_class (directly or indirectly), but
            obj's own class is not a_class itself, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
