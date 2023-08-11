#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:  # Step 1
        for num in row:  # Step 2
            print("{:d}".format(num), end=" ")  # Step 3
        print()  # Print a newline character after each row

# Test the function

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

