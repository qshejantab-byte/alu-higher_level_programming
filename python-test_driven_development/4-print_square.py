#!/usr/bin/python3
"""Defines print_square.

Print a square with the character #.

"""


def print_square(size):
    """Print a square of size x size using the character #.

    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
