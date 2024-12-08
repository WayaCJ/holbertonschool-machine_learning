#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division on two matrices.

    Args:
        mat1 (list): The first 2D matrix (list of lists).
        mat2 (list): The second 2D matrix (list of lists).

    Returns:
        tuple: A tuple containing the element-wise sum, difference, product, and quotient.
    """
    # Perform element-wise operations using list comprehensions
    sum_result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    diff_result = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    prod_result = [[mat1[i][j] * mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    quot_result = [[mat1[i][j] / mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    
    return (sum_result, diff_result, prod_result, quot_result)
