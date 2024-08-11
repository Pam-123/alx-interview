#!/usr/bin/python3

def pascal_triangle(n):
  """
  This function generates Pascal's triangle up to the nth row.

  Args:
      n: The number of rows in the Pascal's triangle.

  Returns:
      A list of lists representing the Pascal's triangle, or an empty list if n <= 0.
  """

  # Handle invalid input (n <= 0)
  if n <= 0:
    return []

  # Initialize the triangle with the first row (always [1])
  triangle = [[1]]

  # Iterate through rows 2 to n (inclusive)
  for i in range(1, n):
    # Create the next row by summing adjacent elements from the previous row
    next_row = [1]  # Start with 1 at the beginning
    for j in range(1, i):
      previous_row = triangle[i - 1]
      next_row.append(previous_row[j - 1] + previous_row[j])
    next_row.append(1)  # End with 1
    triangle.append(next_row)

  return triangle
