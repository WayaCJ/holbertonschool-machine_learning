#!/usr/bin/env python3
"""Module that adds"""


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise"""
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) for row1,
        row2 in zip(mat1, mat2)):
        return None

    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))]
            for i in range(len(mat1))]
