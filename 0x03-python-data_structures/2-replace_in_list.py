#!/usr/bin/python3
'''
function that replaces an element of a list at a specific position
@ny_list: the list
@idx: the index whose element is to be printed
@element: the element to replace at the index
return: my_list if index is out of range or negative, nothing otherwise
'''


def replace_in_list(my_list, idx, element):
    length = len(my_list) - 1
    if idx < 0 or idx > length:
        return my_list
    else:
        my_list[idx] = element
        return my_list
