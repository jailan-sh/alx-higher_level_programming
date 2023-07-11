#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    args :filename
          text
    returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        data = myfile.write(text)
        return data
