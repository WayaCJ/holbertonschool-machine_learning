#!/usr/bin/env python3

def np_shape(matrix):
    """
    Returns the shape of a matrix
    """
    try:
        return (len(matrix),) + np_shape(matrix[0])
    except TypeError:
        return (len(matrix),)
