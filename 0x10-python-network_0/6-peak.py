#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak"""
    if list_of_integers == []:
        return None
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return (max(list_of_integers))
    else:
        med = (len(list_of_integers) // 2)
        if list_of_integers[med] >= list_of_integers[med - 1] and
        list_of_integers[med] > list_of_integers[med + 1]:
            return list_of_integers[med]
        elif list_of_integers[med] <= list_of_integers[med - 1]:
            return find_peak(list_of_integers[:med])
        else:
            return find_peak(list_of_integers[med + 1:])
