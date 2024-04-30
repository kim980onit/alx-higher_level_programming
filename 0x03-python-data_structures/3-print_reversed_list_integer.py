#!/usr/bin/python3
'''
function that prints all integers in a list in reverse order
@my_list: the list to print
'''


def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()

        for num in my_list:
            print("{:d}".format(num))
