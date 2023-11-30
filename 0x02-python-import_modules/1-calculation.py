#!/usr/bin/python3

if __name__ == "__main__":
    # Check if the script is being run directly

    import sys
    # Import the sys module to access command-line arguments

    from calculator_1 import add, sub, mul, div
    # Import specific functions from the calculator_1 module

    argv = sys.argv[1:]
    # Get command-line arguments, excluding the script name

    argv_count = len(argv)
    # Count the number of command-line arguments

    operators = ["+", "-", "*", "/"]
    # Define a list of valid operators

    if argv_count != 3:
        # Check if the number of command-line arguments is not equal to 3
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        # Print the correct usage and exit with a non-zero status
        exit(1)
    elif sys.argv[2] not in operators:
        # Check if the specified operator is not in the list of valid operators
        print("Unknown operator. Available operators: +, -, * and /")
        # Print an error message and exit with a non-zero status
        exit(1)
    else:
        # If conditions are met, proceed with calculations

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        # Convert command-line arguments to integers

        if sys.argv[2] == "+":
            # Check the operator and perform addition
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif sys.argv[2] == "-":
            # Check the operator and perform subtraction
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif sys.argv[2] == "*":
            # Check the operator and perform multiplication
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif sys.argv[2] == "/":
            # Check the operator and perform division
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
