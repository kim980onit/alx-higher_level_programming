#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    power = []
    for line in matrix:
        row_power = [pow(c, 2) for c in line]
        power.append(row_power)
    return power