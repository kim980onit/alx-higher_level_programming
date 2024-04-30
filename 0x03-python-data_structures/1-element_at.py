#!/usr/bin/python3
'''
function that prints the element in a list at a certain index
@my_list: the list
@idx: the index to print
return: None if idx is negative or out of range, value at idx otherwise
'''


def element_at(my_list, idx):
    length = len(my_list) - 1
    if idx < 0 or idx > length:
        return "None"
    return my_list[idx]
