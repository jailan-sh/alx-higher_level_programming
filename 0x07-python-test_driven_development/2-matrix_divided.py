#!/usr/bin/python3
"""

Divide a matrix

"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.
    matrix must be a list of lists of integers or floats
    otherwise raise a TypeError"""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if all(isinstance(row, list) and all(isinstance(val, (int, float))
       for val in row) for row in matrix):
        msg = "matrix must be a matrix (list of lists) of integers/float"
        raise TypeError(msg)
    row_len = set(len(row) for row in matrix)
    if len(row_len) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    new = [[round(val / div, 2) for val in row] for row in matrix]
    return new
