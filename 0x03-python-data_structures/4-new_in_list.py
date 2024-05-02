#!/usr/bin/python3
'''
function that replaces an element in a list without modifying the list
@my_list: the list
@idx: the index to replace
@element: the element to replace the element at idx with
return: my_list if idx < 0 or out of bounds, new_list otherwise
'''


def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    if idx < 0 or idx > length:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list

