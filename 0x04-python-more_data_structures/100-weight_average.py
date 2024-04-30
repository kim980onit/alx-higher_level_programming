#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_sum = 0
    weighted_len = 0
    if not my_list:
        return 0
    for tup in my_list:
        tup_product = 1
        for el in tup:
            tup_product *= el
        weighted_sum += tup_product
        weighted_len += tup[1]
    return weighted_sum / weighted_len