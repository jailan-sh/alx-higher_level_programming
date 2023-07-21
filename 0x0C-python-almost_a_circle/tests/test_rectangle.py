#!/usr/bin/python3
"""test module for rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch


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

class Test_x(unittest.TestCase):
    """ Class for unittest of x """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_xintpos(self):
        """ Positive Int for x """
        r1 = Rectangle(1, 1, 5)
        self.assertEqual(r1.x, 5)

    def test_xintneg(self):
        """ Negative Int for x """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, -5)

    def test_xintzero(self):
        """ Zero Int for x """
        r1 = Rectangle(1, 1, 0)
        self.assertEqual(r1.x, 0)

    def test_xfloat(self):
        """ pos float for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1.0)

    def test_xfloatneg(self):
        """ neg float for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, -1.0)

    def test_xNone(self):
        """ None for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, None)

    def test_xStr(self):
        """ Str for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, "1")

    def test_xList(self):
        """ List for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, [1])

    def test_xTuple(self):
        """ Tuple for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, (1, ))

    def test_xSet(self):
        """ Set for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, {1})

    def test_xprivate(self):
        """ Check private x """
        r1 = Rectangle(1, 1, 5)
        self.assertEqual(r1.x, 5)
        with self.assertRaises(AttributeError):
            r1.__x


class Test_y(unittest.TestCase):
    """ Class for unittest of y """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_yintpos(self):
        """ Positive Int for y """
        r1 = Rectangle(1, 1, 1, 5)
        self.assertEqual(r1.y, 5)

    def test_yintneg(self):
        """ Negative Int for y """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, 1, -5)

    def test_yintzero(self):
        """ Zero Int for y """
        r1 = Rectangle(1, 1, 1, 0)
        self.assertEqual(r1.y, 0)

    def test_yfloat(self):
        """ pos float for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1.0)

    def test_yfloatneg(self):
        """ neg float for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, -1.0)

    def test_yNone(self):
        """ None for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, None)

    def test_yStr(self):
        """ Str for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, "1")

    def test_yList(self):
        """ List for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, [1])

    def test_yTuple(self):
        """ Tuple for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, (1, ))

    def test_ySet(self):
        """ Set for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, {1})

    def test_yprivate(self):
        """ Check private y """
        r1 = Rectangle(1, 1, 1, 5)
        self.assertEqual(r1.y, 5)
        with self.assertRaises(AttributeError):
            r1.__y


class Test_area(unittest.TestCase):
    """ Class for unittest of area method """

    def test_area1(self):
        """ Area 1 """
        r1 = Rectangle(2, 5)
        self.assertEqual(r1.area(), 10)

    def test_area2(self):
        """ Area 2 """
        r1 = Rectangle(1, 4)
        self.assertEqual(r1.area(), 4)

    def test_area3(self):
        """ Area 2 """
        r1 = Rectangle(3, 3, 1, 1, 1)
        self.assertEqual(r1.area(), 9)

class Test_update(unittest.TestCase):
    """ Class for unittest of update method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_noargs(self):
        """ Did not Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update()
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 6)

    def test_upid(self):
        """ Id Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_upwidth(self):
        """ Width Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, 12)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_upheight(self):
        """ Height Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, 12, 8)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_upx(self):
        """ X Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, 12, 8, 0)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_upy(self):
        """ Y Update """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, 12, 8, 0, 7)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 7)
        self.assertEqual(r1.id, 85)

    def test_Kignore(self):
        """ Ignore Kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(85, id=15, width=16, height=17, x=18, y=19)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 85)

    def test_Kid(self):
        """ id kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(id=15)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 15)

    def test_Kwidth(self):
        """ width kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(width=16, id=15)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 15)

    def test_Kheight(self):
        """ height kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(width=16, id=15, height=17)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 15)

    def test_Kx(self):
        """ x kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(x=18, width=16, id=15, height=17)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 18)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 15)

    def test_Ky(self):
        """ y kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(x=18, width=16, y=19, id=15, height=17)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 18)
        self.assertEqual(r1.y, 19)
        self.assertEqual(r1.id, 15)

    def test_Kfullchange(self):
        """ Full change kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        r1.update(id=15, width=16, height=17, x=18, y=19)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 18)
        self.assertEqual(r1.y, 19)
        self.assertEqual(r1.id, 15)

    def test_Kfullchange2(self):
        """ Full change kwargs """
        r1 = Rectangle(2, 3, 4, 5, 6)
        d1 = {"id": 15, "width": 16, "height": 17, "x": 18, "y": 19}
        r1.update(**d1)
        self.assertEqual(r1.width, 16)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 18)
        self.assertEqual(r1.y, 19)
        self.assertEqual(r1.id, 15)
