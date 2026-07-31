#!/usr/bin/python3
"""Module that defines a function to check class membership by heritage."""


def is_kind_of_class(obj, a_class):
    """Check whether an object is an instance of a class or its heirs.

    Args:
        obj: The object to check.
        a_class: The class (or ancestor class) to compare against.

    Returns:
        bool: True if obj is an instance of a_class, or of a
            subclass of a_class, else False.
    """
    return isinstance(obj, a_class)
