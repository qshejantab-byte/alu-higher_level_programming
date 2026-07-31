#!/usr/bin/python3
"""Module that defines a BaseGeometry class with value validation."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Compute the area of the shape.

        Raises:
            Exception: Always, since this is meant to be overridden
                by a subclass that represents a concrete shape.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated, used
                in any error message that gets raised.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
