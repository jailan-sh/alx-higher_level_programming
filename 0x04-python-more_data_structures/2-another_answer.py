#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_a = set(my_list)
    newlist = list(set_a)
    return sum(newlist)
