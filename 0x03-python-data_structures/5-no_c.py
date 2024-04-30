#!/usr/bin/python3
'''
function that removes of occurrencies of 'c' and 'C' from a string
@my_string: string to analyse
return: my_string without 'c' and 'C'
'''


def no_c(my_string):
    new_string = ''
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        else:
            new_string += char
    return new_string