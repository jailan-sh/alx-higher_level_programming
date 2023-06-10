#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        newlist = list(my_string)
        [newlist.remove(alph) for alph in newlist if alph == 'c' or alph == 'C']
        return("".join(newlist))
