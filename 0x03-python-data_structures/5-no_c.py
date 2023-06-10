#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = ""
        for alph in my_string:
            if alph not in ["C", "c"]:
                new_string += alph
        return(new_string)
