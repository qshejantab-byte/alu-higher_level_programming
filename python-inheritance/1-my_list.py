#!/usr/bin/python3
"""Module that defines a list subclass with a sorted-print method."""


class MyList(list):
    """A list that can print itself in ascending sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order.

        Assumes every element of the list is an integer. The list
        itself is left unchanged.
        """
        print(sorted(self))
