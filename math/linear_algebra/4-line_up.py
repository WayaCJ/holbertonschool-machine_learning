#!/usr/bin/env python3
"""Module that adds"""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise"""
    if len(arr1) != len(arr2):  # Check if arrays are not of the same length
        return None

    return [a + b for a, b in zip(arr1, arr2)]
