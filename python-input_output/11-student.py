#!/usr/bin/python3
"""Module that defines a Student class with JSON reload support."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student.

        Args:
            attrs (list): An optional list of attribute names to
                include. If not a list of strings, every attribute
                is included instead.

        Returns:
            dict: The requested attributes of the student.
        """
        if isinstance(attrs, list) and all(
                isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the student's attributes from a dictionary.

        Args:
            json (dict): A mapping of attribute names to values.
                Every key becomes a public attribute on the student.
        """
        for key, value in json.items():
            setattr(self, key, value)
