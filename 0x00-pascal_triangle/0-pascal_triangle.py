#!/usr/bin/python3
"""
Module to generate Pascal's Triangle.

This module provides a function that generates Pascal's Triangle up to the nth row.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list of lists: A list of lists of integers representing Pascal's Triangle.
                       Each inner list represents a row in the triangle.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the first row
    
    for i in range(1, n):
        prev_row = triangle[-1]
        # Start the new row with a 1
        new_row = [1]
        # Generate the intermediate values by adding the adjacent elements in the previous row
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        # End the new row with a 1
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle
