#!/usr/bin/python3
"""test module for rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_arguments(unittest.TestCase):
    """ test models for args of Rectangle class"""
    def setup(self):
        """set up for all methods"""
        Self.__Base__nb_objects =0

    def test_id(self):
        """for testing id"""
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.id, 1)

    def test_noid(self):
        """ no id"""
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.id, 2)

