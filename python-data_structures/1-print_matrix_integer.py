# #!/usr/bin/python3
# def print_matrix_integer(matrix=[[]]):
#     for row in matrix:
#         for num in row:
#             print("{:d}".format(num), sep=",", end=[-1] " ")
#         print()
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print_matrix_integer(matrix)

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end="" if i == len(row) - 1 else " ")
        print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix_integer(matrix)
