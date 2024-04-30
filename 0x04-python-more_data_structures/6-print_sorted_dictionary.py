#!/usr/bin/python3
'''
function that prints a dictinary by ordered keys
'''


def print_sorted_dictionary(a_dictionary):
    for item in sorted(a_dictionary):
        print("{:s}: {}".format(item, a_dictionary[item]))