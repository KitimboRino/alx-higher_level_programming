#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays
the body of the response.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
from sys import argv
import requests

if __name__ == "__main__":
    # Extracting URL from command line argument
    url = argv[1]

    # Sending a GET request to the provided URL
    req = requests.get(url)

    # Checking if the status code indicates an error
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        # Printing the body of the response
        print(req.text)
