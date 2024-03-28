#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the
body of the response (decoded in utf-8).

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    # Extracting URL from command line argument
    url = argv[1]

    # Creating a request object with the provided URL
    req = Request(url)

    try:
        # Sending the request and handling the response
        with urlopen(req) as response:
            # Decoding and printing the body of the response
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        # Handling HTTP errors and printing the error code
        print("Error code: {}".format(e.code))
