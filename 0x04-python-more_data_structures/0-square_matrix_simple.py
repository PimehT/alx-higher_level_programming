#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    This function takes a matrix and returns the new matrix with items squared

    Parameters: matrix to square
    type: list (list of lists)
    example: [[1,2],[3,4]]
    Returns: squared matrix
    """
    squared = []
    if len(matrix) == 0:
        return
    if not matrix:
        return
    for row in matrix:
        squared.append([i ** 2 for i in row])

    return squared
