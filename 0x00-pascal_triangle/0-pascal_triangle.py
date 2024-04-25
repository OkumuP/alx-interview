#!/usr/bin/python3
""" Create a function that returns integers representing the Pascal's triangle of n """


def pascal_triangle(n):
    """ create a pascal triangle
    n: number of rows
    return:
        Pascal's triangle """
    new_pascal = []

    """ Assume n is an int """
    if n <= 0:
        return new_pascal

    for i in range(n):
        row_index = [1]
        if new_pascal:
            final_row = new_pascal[-1]
            row_index.extend([sum(pair) for pair in
                              zip(final_row, final_row[1:])])
            row_index.append(1)
        new_pascal.append(row_index)
    return (new_pascal)
