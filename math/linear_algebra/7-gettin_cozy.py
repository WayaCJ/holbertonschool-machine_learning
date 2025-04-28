#!/usr/bin/env python3
"""Module that concatenates two matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis"""
    if axis == 0:
        if len(mat1[0]) == len(mat2[0]):  # Same number of columns
            return mat1 + mat2  # Concatenate rows
        else:
            return None

    elif axis == 1:
        if len(mat1) == len(mat2):  # Same number of rows
            return [row1 + row2 for row1,
                    row2 in zip(mat1, mat2)]
        else:
            return None

    return None
