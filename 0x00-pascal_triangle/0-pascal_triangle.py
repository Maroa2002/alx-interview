#!/usr/bin/python3
'''
    Generating the Pascal's triangle
    Args:
        n: number of rows
    return:
        list of lists representing pascals triangle
'''


def pascal_triangle(n):
    triangle = []

    if (n <= 0):
        return []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
