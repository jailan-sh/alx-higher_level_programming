#!/usr/bin/python3
""" read file"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    args : filename
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        print(myfile.read(), end='')
