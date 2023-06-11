#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newtuple = ()
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        newtuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif len(tuple_a) >= 2 and len(tuple_b) == 1:
        newtuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    elif len(tuple_a) >= 2 and len(tuple_b) == 0:
        newtuple = (tuple_a[0], tuple_a[1])
    elif len(tuple_a) == 1 and len(tuple_b) >= 2:
        newtuple = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
    elif len(tuple_a) == 0 and len(tuple_b) >= 2:
        newtuple = (tuple_b[0], tuple_b[1])
    else:
        newtuple = (0, 0)
    return newtuple
