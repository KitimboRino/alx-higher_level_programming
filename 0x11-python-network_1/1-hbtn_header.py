#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    # Extracting URL from command line argument
    url = argv[1]

    # Creating a request object with the provided URL
    req = Request(url)

    # Sending the request and handling the response
    with urlopen(req) as response:
        # Extracting and printing the value of X-Request-Id header
        print(dict(response.headers).get("X-Request-Id"))
