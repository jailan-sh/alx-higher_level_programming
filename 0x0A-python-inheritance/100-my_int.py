#!/usr/bin/python3
""" class inherted int class """


class MyInt(int):
    """ class MyInt"""
    def __eq__(self, other):
        """Call to Not Equal """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Call to Equal """
        return super().__eq__(other)
