#!/usr/bin/python3
'''
Function to prints all integers in a list
@my_list=[] : list from which to print number
'''


def print_list_integer(my_list=[]):
    for num in my_list:
        print("{:d}".format(num))
