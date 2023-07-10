#!/usr/bin/python3
"""
class Mylist
"""


class MyList(list):
    """
    a subclass MyList
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
