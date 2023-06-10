#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        rows = []
        for row in matrix:
            new_str = " ".join(str(i) for i in row)
            ele = "".join(new_str)
            print("{:s}".format(ele))
