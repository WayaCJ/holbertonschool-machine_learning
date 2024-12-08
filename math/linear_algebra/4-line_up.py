#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):  # Check if arrays are not of the same length
        return None

    return [a + b for a, b in zip(arr1, arr2)]
