#!/usr/bin/env python3

def matrix_shape(matrix):
    if isinstance(matrix, list) and matrix:  # Check if the matrix is a non-empty list
        return [len(matrix)] + matrix_shape(matrix[0]) if isinstance(matrix[0], list) else [len(matrix)]
    return []
