#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys in a_dictionary:
        print("{}: {}".format(keys.sort(), a_dictionary[keys]))
