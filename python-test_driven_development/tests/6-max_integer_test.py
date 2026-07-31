#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """List where values increase in order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """List where the max is not last."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_first(self):
        """List where the max is first."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """List with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Empty list returns None."""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """No argument uses the default (empty) list."""
        self.assertEqual(max_integer(), None)

    def test_negative_numbers(self):
        """List of negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_positive_negative(self):
        """List with both positive and negative numbers."""
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_all_same_values(self):
        """List where all elements are equal."""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_floats(self):
        """List of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == "__main__":
    unittest.main()
