#!/usr/bin/python3
'''
function that replaces or adds key/value in a dictionary
if key exits, value would be replaced
if key does not exits, key would be created
'''


def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary