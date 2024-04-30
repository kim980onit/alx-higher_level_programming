#!/usr/bin/python3
'''
function that returns a new dictionary with all values multiplied by 2
'''


def multiply_by_2(a_dictionary):
    new = {}
    for i in a_dictionary:
        new[i] = a_dictionary[i] * 2
    return new