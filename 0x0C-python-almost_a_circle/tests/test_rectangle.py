#!/usr/bin/python3
"""test module for rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_args(unittest.TestCase):
    """ Class for unittest of arguments """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_nowidth(self):
        """ Test for no width """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_noheight(self):
        """ Test for no height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_nox(self):
        """ Test for no x """
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.x, 0)

    def test_noy(self):
        """ Test for no y """
        r1 = Rectangle(1, 1, 1)
        self.assertEqual(r1.y, 0)

    def test_noid(self):
        """ Test for no id """
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.id, 1)

    def test_id(self):
        """ Test for id """
        r1 = Rectangle(1, 1, 1, 1, 85)
        self.assertEqual(r1.id, 85)

    def test_extraarg(self):
        """ Test for no extra arguments """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1, 1, 1)

class Test_width(unittest.TestCase):
    """ Class for unittest of width """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_widthintpos(self):
        """ Positive Int for Width """
        r1 = Rectangle(5, 1)
        self.assertEqual(r1.width, 5)
        with self.assertRaises(AttributeError):
            r1.__width

    def test_widthintneg(self):
        """ Negative Int for Width """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-5, 1)

    def test_widthintzero(self):
        """ Zero Int for Width """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 1)

    def test_widthfloat(self):
        """ float for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1.0, 1)

    def test_widthNone(self):
        """ None for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 1)

    def test_widthStr(self):
        """ Str for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 1)

    def test_widthList(self):
        """ List for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle([1], 1)

    def test_widthTuple(self):
        """ Tuple for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle((1, ), 1)

    def test_widthSet(self):
        """ Set for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle({1}, 1)

class Test_height(unittest.TestCase):
    """ Class for unittest of height """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_heightintpos(self):
        """ Positive Int for height """
        r1 = Rectangle(1, 5)
        self.assertEqual(r1.height, 5)

    def test_heightintneg(self):
        """ Negative Int for height """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -5)

    def test_heightintzero(self):
        """ Zero Int for height """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

    def test_heightfloat(self):
        """ float for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1.0)


        """ None for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, None)

    def test_heightStr(self):
        """ Str for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "1")

    def test_heightList(self):
        """ List for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, [1])

    def test_heightTuple(self):
        """ Tuple for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, (1, ))

    def test_heightSet(self):
        """ Set for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, {1})

    def test_heightprivate(self):
        """ Check private Width """
        r1 = Rectangle(1, 5)
        self.assertEqual(r1.height, 5)
        with self.assertRaises(AttributeError):
            r1.__height

