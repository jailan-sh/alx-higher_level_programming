#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        for alph in my_string:
            if alph == "c" or alph == "C":
                my_string = my_string.replace(alph, "")
        return(my_string)
