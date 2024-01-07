#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        """Test when the list is in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test when the list is not in ascending order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test when the list is empty."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test when the list contains only negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -7]), -1)

    def test_duplicate_max_value(self):
        """Test when the list has duplicate maximum values."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_single_element_list(self):
        """Test when the list has only one element."""
        self.assertEqual(max_integer([42]), 42)

    def test_mixed_positive_negative(self):
        """Test when the list has mixed positive and negative numbers."""
        self.assertEqual(max_integer([10, -3, 8, -5]), 10)

if __name__ == '__main__':
    unittest.main()
