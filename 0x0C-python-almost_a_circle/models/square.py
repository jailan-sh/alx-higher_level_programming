#!/usr/bin/python3
""" square class which inherited Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square module """
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ Print Method """
        st = "[Square] ({:d}) {:d}/{:d} - {:d}"
        st = st.format(self.id, self.x, self.y, self.width)
        return st

    def update(self, *args, **kwargs):
        """  assigns an argument to each attribute"""
        mylist = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(mylist):
                    setattr(self, mylist[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """func. Returns dicitionary representation of Square """
        sdict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return sdict
