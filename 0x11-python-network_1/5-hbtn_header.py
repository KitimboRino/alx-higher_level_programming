#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the
value of the variable X-Request-Id in the response header.

Usage: ./5-hbtn_header.py <URL>
"""
import requests
from sys import argv

if __name__ == "__main__":
    # Extracting URL from command line argument
    url = argv[1]

    # Sending a GET request to the provided URL
    req = requests.get(url)

    # Printing the value of X-Request-Id header
    print(req.headers.get("X-Request-Id"))
