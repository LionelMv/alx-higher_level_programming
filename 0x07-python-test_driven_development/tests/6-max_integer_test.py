#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1.2, -2.2]), -1.2)
        self.assertEqual(max_integer([3, -3, 3]), 3)

    def test_list_of_strings(self):
        self.assertEqual(max_integer("Lionel"), "o")
        self.assertEqual(max_integer("1234"), "4")
        self.assertEqual(max_integer(["a", "c", "x", "y"]), "y")
        self.assertEqual(max_integer("abc", "q"), "q")

if __name__ == "__main__":
    unittest.main()