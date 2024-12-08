#!/usr/bin/env python3

def np_shape(matrix):
    """
    Calculates the shape of a 2D matrix (list of lists).
    
    Args:
        matrix (list): A 2D matrix represented as a list of lists.
    
    Returns:
        tuple: The shape of the matrix (number of rows, number of columns).
    """
    if not matrix:  # If the matrix is empty
        return (0,)

    # Number of rows (outer list length)
    num_rows = len(matrix)
    
    # Number of columns (assuming all rows are of equal length)
    num_cols = len(matrix[0]) if matrix else 0
    
    return (num_rows, num_cols)
