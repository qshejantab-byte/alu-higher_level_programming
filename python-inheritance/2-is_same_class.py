#!/usr/bin/python3
"""Module that defines a function to check exact class membership."""


def is_same_class(obj, a_class):
    """Check whether an object is exactly an instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if type(obj) is exactly a_class, else False.
    """
    return type(obj) is a_class
