#!/usr/bin/python3
# 12-pascal_triangle.py
""" returns a list of lists forming pascal's triangle """


def pascal_triangle(n):
    """
    Returns a list of lists forming pascal's triangle
    0, 1, 1, 2, 3, ... n rows in the triangle
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, len(row) - 1):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
