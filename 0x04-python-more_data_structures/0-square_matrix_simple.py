#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        squre_row = list(map(lambda x: x * x, i))
        new_matrix.append(squre_row)
    return new_matrix
