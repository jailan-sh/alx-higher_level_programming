#!/usr/bin/python3
"""pascal_triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    pasical = []
    if n <= 0:
        return pasical
    else:
        for i in range(n):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(pasical[i - 1][j - 1] + pasical[i - 1][j])
            pasical.append(temp)
    return pasical
