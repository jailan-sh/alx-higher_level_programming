#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = []
    for i in my_list:
        if i not in a:
            a.append(i)
    return sum(a)
