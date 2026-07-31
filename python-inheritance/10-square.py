#!/usr/bin/python3
"""Module that defines a Square class based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square as a special case of a rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The length of each side of the square. Must
                be a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
