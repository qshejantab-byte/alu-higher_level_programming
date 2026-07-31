#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Compute the area of the shape.

        Raises:
            Exception: Always, since this is meant to be overridden
                by a subclass that represents a concrete shape.
        """
        raise Exception("area() is not implemented")
