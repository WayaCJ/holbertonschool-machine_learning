#!/usr/bin/env python3
import numpy as np

def np_elementwise(mat1, mat2):
    sum_result = mat1 + mat2
    diff_result = mat1 - mat2
    prod_result = mat1 * mat2
    quot_result = mat1 / mat2

    return (sum_result, diff_result, prod_result, quot_result)
