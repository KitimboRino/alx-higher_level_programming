#!/usr/bin/python3
def weight_average(my_list=[]):
    # Check for empty list
    if not my_list:
        return 0

    # Initialize variables
    total_score = 0
    total_weight = 0

    # Iterate through each tuple in the list
    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    # Calculate the weighted average
    weighted_average = total_score / total_weight

    return weighted_average
