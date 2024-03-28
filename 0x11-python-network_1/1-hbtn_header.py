#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""


from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    # Get the URL from command-line argument
    url = argv[1]

    # Create a Request object with the URL
    req = Request(url)

    # Open the request using urlopen
    with urlopen(req) as response:
        # Get the X-Request-Id variable from the response headers
        x_request_id = dict(response.headers).get("X-Request-Id")

        # Check if X-Request-Id variable is present in the header
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id variable not found in header of response.")
