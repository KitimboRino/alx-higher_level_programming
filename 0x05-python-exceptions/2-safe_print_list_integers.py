def safe_print_list_integers(my_list=[], x=0):
    # Initialize a variable to count the number of integers printed
    count = 0
    
    try:
        # Use a for loop to iterate through the list up to the specified number of elements (x)
        for i in range(x):
            # Try to convert the element to an integer and print if successful
            try:
                print("{:d}".format(int(my_list[i])), end="")
                count += 1
            except (ValueError, TypeError):
                # Catch ValueError (if the element cannot be converted to an integer) or TypeError
                # Do nothing in this case (skip the non-integer value)
                pass
    except IndexError:
        # Catch IndexError if we try to access an index beyond the length of the list
        pass
    finally:
        # Ensure a newline is printed after the integers, whether an exception occurred or not
        print()
    
    # Return the real number of integers printed
    return count
