#!/usr/bin/python3
""" 
Unittest for base class
"""

import unittest
from models.base import Base

class Test_id(unittest.TestCase):
    """ Class for unittest of __init__ and id """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_no_arg(self):
        """ Id no argument """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_none(self):
        """ Id None """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_ints(self):
        """ Id int """
        b1 = Base(5)
        self.assertEqual(b1.id, 5)
        b2 = Base(-5)
        self.assertEqual(b2.id, -5)
