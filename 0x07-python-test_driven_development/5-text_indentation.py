#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after each of these characters:
. ? and :

"""


def text_indentation(text):
    """
    Prints a text replace some characters with 2 newlines
    Arg:
    text: must be a string
    If not a string a TypeError is raised
    There is no space at the beginning at the end of each printed line
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    indented_text = ""
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            indented_text += text[i] + "\n\n"
        else:
            indented_text += text[i]
    print(indented_text)
