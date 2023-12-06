#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check for invalid input
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Create a dictionary to map Roman numerals to integers
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Initialize total sum
    total = 0

    # Iterate through the Roman string
    for i in range(len(roman_string)):
        # If the current numeral is smaller than the next numeral, subtract its value
        if i < len(roman_string) - 1 and roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            total -= roman_dict[roman_string[i]]
        else:
            total += roman_dict[roman_string[i]]

    return total
