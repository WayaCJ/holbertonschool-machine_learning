#!/usr/bin/env python3
"""Module that calculates"""


def matrix_shape(matrix):
    """Calculates the shape of a matrix"""
    if isinstance(matrix, list) and matrix:
        if isinstance(matrix[0], list):
            return [len(matrix)] + matrix_shape(matrix[0])
        else:
            return [len(matrix)]
    return []
