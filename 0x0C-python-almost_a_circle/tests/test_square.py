#!/usr/bin/python3
""" Unittest for square class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_argsS(unittest.TestCase):
    """ Class for unittest of arguments """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_noSize(self):
        """ Test for no width """
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_noxS(self):
        """ Test for no x """
        s1 = Square(1)
        self.assertEqual(s1.x, 0)

    def test_noyS(self):
        """ Test for no y """
        s1 = Square(1, 1)
        self.assertEqual(s1.y, 0)

    def test_noidS(self):
        """ Test for no id """
        s1 = Square(1, 1, 1)
        self.assertEqual(s1.id, 1)

    def test_idS(self):
        """ Test for id """
        s1 = Square(1, 1, 1, 85)
        self.assertEqual(s1.id, 85)

    def test_extraargS(self):
        """ Test for no extra arguments """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, 1, 1, 1)


class Test_size(unittest.TestCase):
    """ Class for unittest of size """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_sizeintpos(self):
        """ Positive Int for size """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_sizeintneg(self):
        """ Negative Int for size """
        with self.assertRaises(ValueError):
            s1 = Square(-5)

    def test_sizeintzero(self):
        """ Zero Int for size """
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_widthfloat(self):
        """ pos float for size """
        with self.assertRaises(TypeError):
            s1 = Square(1.0)

    def test_sizefloatneg(self):
        """ neg float for size """
        with self.assertRaises(TypeError):
            s1 = Square(-1.0)

    def test_sizeNone(self):
        """ None for size """
        with self.assertRaises(TypeError):
            s1 = Square(None)

    def test_widthStr(self):
        """ Str for size """
        with self.assertRaises(TypeError):
            s1 = Square("1")

    def test_widthList(self):
        """ List for size """
        with self.assertRaises(TypeError):
            s1 = Square([1])

    def test_widthTuple(self):
        """ Tuple for size """
        with self.assertRaises(TypeError):
            s1 = Square((1, ))

    def test_widthSet(self):
        """ Set for size """
        with self.assertRaises(TypeError):
            s1 = Square({1})

    def test_widthprivate(self):
        """ Check private size """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        with self.assertRaises(AttributeError):
            s1.__size


class Test_xS(unittest.TestCase):
    """ Class for unittest of x """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_xintposS(self):
        """ Positive Int for x """
        s1 = Square(1, 5)
        self.assertEqual(s1.x, 5)

    def test_xintnegS(self):
        """ Negative Int for x """
        with self.assertRaises(ValueError):
            s1 = Square(1, -5)

    def test_xintzeroS(self):
        """ Zero Int for x """
        s1 = Square(1, 0)
        self.assertEqual(s1.x, 0)

    def test_xfloatS(self):
        """ pos float for x """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1.0)

    def test_xfloatnegS(self):
        """ neg float for x """
        with self.assertRaises(TypeError):
            s1 = Square(1, -1.0)

    def test_xNoneS(self):
        """ None for x """
        with self.assertRaises(TypeError):
            s1 = Square(1, None)

    def test_xStrS(self):
        """ Str for x """
        with self.assertRaises(TypeError):
            s1 = Square(1, "1")

    def test_xListS(self):
        """ List for x """
        with self.assertRaises(TypeError):
            s1 = Square(1, [1])

    def test_xTupleS(self):
        """ Tuple for x """
        with self.assertRaises(TypeError):
            s1 = Square(1, (1, ))

    def test_xSetS(self):
        """ Set for x """
        with self.assertRaises(TypeError):
            s1 = Square(1, {1})

    def test_xprivateS(self):
        """ Check private x """
        s1 = Square(1, 5)
        self.assertEqual(s1.x, 5)
        with self.assertRaises(AttributeError):
            s1.__x


class Test_yS(unittest.TestCase):
    """ Class for unittest of y """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_yintposS(self):
        """ Positive Int for y """
        s1 = Square(1, 1, 5)
        self.assertEqual(s1.y, 5)

    def test_yintnegS(self):
        """ Negative Int for y """
        with self.assertRaises(ValueError):
            s1 = Square(1, 1, -5)

    def test_yintzeroS(self):
        """ Zero Int for y """
        s1 = Square(1, 1, 0)
        self.assertEqual(s1.y, 0)

    def test_yfloatS(self):
        """ pos float for y """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, 1.0)

    def test_yfloatnegS(self):
        """ neg float for y """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, -1.0)

    def test_yNoneS(self):
        """ None for y """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, None)

    def test_yStrS(self):
        """ Str for y """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, "1")

    def test_yListS(self):
        """ List for y """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, [1])

    def test_yTupleS(self):
        """ Tuple for y """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, (1, ))

    def test_ySetS(self):
        """ Set for y """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, {1})

    def test_yprivateS(self):
        """ Check private y """
        s1 = Square(1, 1, 5)
        self.assertEqual(s1.y, 5)
        with self.assertRaises(AttributeError):
            s1.__y


class Test_areaS(unittest.TestCase):
    """ Class for unittest of area method """

    def test_area1S(self):
        """ Area 1 """
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)

    def test_area2(self):
        """ Area 2 """
        s1 = Square(1)
        self.assertEqual(s1.area(), 1)

    def test_area3(self):
        """ Area 3 """
        s1 = Square(3, 1, 1, 1)
        self.assertEqual(s1.area(), 9)

class Test_updateS(unittest.TestCase):
    """ Class for unittest of update method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_noargsS(self):
        """ Did not Update """
        s1 = Square(3, 4, 5, 6)
        s1.update()
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 6)

    def test_upidS(self):
        """ Id Update """
        s1 = Square(2, 4, 5, 6)
        s1.update(85)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 85)

    def test_upsize(self):
        """ Size Update """
        s1 = Square(3, 4, 5, 6)
        s1.update(85, 12)
        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 85)

    def test_upxS(self):
        """ X Update """
        s1 = Square(3, 4, 5, 6)
        s1.update(85, 12, 0)
        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 85)

    def test_upyS(self):
        """ Y Update """
        s1 = Square(3, 4, 5, 6)
        s1.update(85, 12, 0, 7)
        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 7)
        self.assertEqual(s1.id, 85)

    def test_KignoreS(self):
        """ Ignore Kwargs """
        s1 = Square(3, 4, 5, 6)
        s1.update(85, id=15, size=16, x=18, y=19)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 85)

    def test_KidS(self):
        """ id kwargs """
        s1 = Square(3, 4, 5, 6)
        s1.update(id=15)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 15)

    def test_KwidthS(self):
        """ width kwargs """
        s1 = Square(3, 4, 5, 6)
        s1.update(size=16, id=15)
        self.assertEqual(s1.size, 16)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 15)

    def test_KxS(self):
        """ x kwargs """
        s1 = Square(3, 4, 5, 6)
        s1.update(x=18, size=16, id=15)
        self.assertEqual(s1.size, 16)
        self.assertEqual(s1.x, 18)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 15)

    def test_KyS(self):
        """ y kwargs """
        s1 = Square(3, 4, 5, 6)
        s1.update(x=18, size=16, y=19, id=15)
        self.assertEqual(s1.size, 16)
        self.assertEqual(s1.x, 18)
        self.assertEqual(s1.y, 19)
        self.assertEqual(s1.id, 15)

    def test_KfullchangeS(self):
        """ Full change kwargs """
        s1 = Square(3, 4, 5, 6)
        s1.update(id=15, size=16, x=18, y=19)
        self.assertEqual(s1.size, 16)
        self.assertEqual(s1.x, 18)
        self.assertEqual(s1.y, 19)
        self.assertEqual(s1.id, 15)

    def test_Kfullchange2S(self):
        """ Full change kwargs """
        s1 = Square(3, 4, 5, 6)
        d1 = {"id": 15, "size": 16, "x": 18, "y": 19}
        s1.update(**d1)
        self.assertEqual(s1.size, 16)
        self.assertEqual(s1.x, 18)
        self.assertEqual(s1.y, 19)
        self.assertEqual(s1.id, 15)
