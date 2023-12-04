#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Check if the matrix is empty
    if not matrix:
        print()
    else:
        # Iterate through each row of the matrix
        for row in range(len(matrix)):
            # Iterate through each item in the row
            for item in range(len(matrix[row])):
                # Determine whether to print a space or not
                if item != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''

                # Print each element using str.format()
                print("{:d}".format(matrix[row][item]), end=endspace)

            # Move to the next line after printing a row
            print()
