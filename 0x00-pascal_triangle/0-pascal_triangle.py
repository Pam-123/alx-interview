#!/usr/bin/python3
def pascalsTriangle():
    height = int(input("Enter height of triangle:"))
    t_List = []

    for R in range(height):
        n_List = []
        for C in range(R + 1):
            if C == 0 or C == R:
                n_List.append(1)
            else:
                # Sum the two values from the previous row
                n_List.append(t_List[R - 1][C - 1] + t_List[R - 1][C])
        t_List.append(n_List)

    # Print the triangle
    for row in t_List:
        print(row)

# Call the function to see the output
pascalsTriangle()
