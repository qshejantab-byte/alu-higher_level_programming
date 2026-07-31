#!/usr/bin/python3
"""Defines matrix_divided.

Divide all elements of a matrix by a number.

"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(n, (int, float)) and not isinstance(n, bool)
                    for row in matrix for n in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(n / div, 2) for n in row] for row in matrix]
    return new_matrix
