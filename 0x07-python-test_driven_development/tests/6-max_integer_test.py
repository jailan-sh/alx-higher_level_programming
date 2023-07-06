#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Class for unittest of max_integer function"""

    def test_max_intlist(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([1.1, 2.5, 3.1, 4.9]), 4.9)
        self.assertEqual(max_integer([-1.05, -2.2, -3.5, -4.0]), -1.05)
        self.assertEqual(max_integer([-1.8, 2.1, 3.6, -4.1]), 3.6)
        self.assertEqual(max_integer([-1, 2.1, 3, -4.1]), 3)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([5.5]), 5.5)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([5.5, 5.5, 5.5]), 5.5)
        self.assertEqual(max_integer([i for i in range(10)]), 9)
        self.assertEqual(max_integer((-1, 2.1, 3, -4.1)), 3)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer({0: -3, 1: 1.5, 2: 5}), 5)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])
        self.assertEqual(max_integer(["1", "2", "a", "4"]), 'a')

    def test_values(self):
        """Make sure right errors are raised for wrong data types passed"""

        self.assertRaises(TypeError, max_integer, 12)
        self.assertRaises(TypeError, max_integer, True)
