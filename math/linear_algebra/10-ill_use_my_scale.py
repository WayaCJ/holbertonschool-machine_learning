#!/usr/bin/env python3

def np_shape(matrix):
    """
    Returns the shape of a matrix
    """
    return (len(matrix),) + np_shape(matrix[0]) * isinstance(matrix[0], list)
