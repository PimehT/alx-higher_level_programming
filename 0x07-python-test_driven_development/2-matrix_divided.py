#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list[list]): List of lists of integers or floats
        representing the matrix.
        div (int/float): Divisor by which each element
        in the matrix will be divided.

    Raises:
        TypeError:
        1. If the matrix is not a list of lists,
        or any element within is not an int or float.
        2. If each row of the matrix is not of the same size,
        or div is not an int or float.
        ZeroDivisionError: If div is zero.

    Returns:
        list[list]: New matrix with each element divided by div,
        rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) or
                any(not isinstance(ele, (int, float))
                    for ele in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
