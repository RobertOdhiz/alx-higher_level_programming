#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = [row[:] for row in matrix]
    for i in range(len(copy)):
        for j in range(len(copy[i])):
            copy[i][j] = copy[i][j] ** 2

    return copy
