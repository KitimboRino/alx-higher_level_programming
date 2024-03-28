#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
from sys import argv
import requests

if __name__ == "__main__":
    # Extracting letter from command line argument if provided
    letter = "" if len(argv) == 1 else argv[1]

    # Sending a POST request to the specified URL with the letter as a parameter
    req = requests.post("http://0.0.0.0:5000/search_user", {"q": letter})

    try:
        # Parsing the response as JSON
        response = req.json()
        if response == {}:
            # If response is empty, print "No result"
            print("No result")
        else:
            # If response contains data, print user ID and name
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        # Handling invalid JSON response
        print("Not a valid JSON")
