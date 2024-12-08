#!/usr/bin/env python3

def np_transpose(matrix):
    """
    Returns the transpose of a matrix (list of lists).
    
    Args:
        matrix (list): A 2D matrix represented as a list of lists.
    
    Returns:
        list: The transposed matrix.
    """
    # Use list comprehension to transpose the matrix
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
