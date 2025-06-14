#!/usr/bin/env python3
"""Module that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication"""
    if len(mat1[0]) != len(mat2):
        return None

    result = []
    for i in range(len(mat1)):  # Iterate through rows of mat1
        row_result = []
        for j in range(len(mat2[0])):  # Iterate through columns of mat2
            dot_produc = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
            row_result.append(dot_produc)
        result.append(row_result)
    return result
