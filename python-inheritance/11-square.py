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

    def __str__(self):
        """Return the printable representation of the square."""
        width = self._Rectangle__width
        height = self._Rectangle__height
        return "[Square] {}/{}".format(width, height)
