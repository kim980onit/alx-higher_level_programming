#!/usr/bin/python3
'''
function that adds all unique integers in a list
@my_list: the list to be summed
return: the sum of unique ints
'''


def uniq_add(my_list=[]):
    sum = 0
    for num in set(my_list):
        sum += num
    return sum