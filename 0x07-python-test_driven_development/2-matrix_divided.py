#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix
    and returns new matrix
Requires same size lists of ints or floats, and max two decimal places
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with dividends
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(message)

    new_matrix = []
    len_first_row = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(message)
        if len(row) != len_first_row:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(message)
            new_row.append(round(i/div, 2))
        new_matrix.append(new_row)
    return new_matrix
