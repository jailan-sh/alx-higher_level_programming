#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = ""
        for alph in my_string:
            if (alph != 'c') and (alph != 'C'):
                new_string += alph
        return(new_string)
