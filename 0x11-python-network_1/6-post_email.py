#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body
of the response.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    # Extracting URL and email address from command line arguments
    url = argv[1]
    email = argv[2]

    # Creating a dictionary containing the email parameter
    value = {"email": email}

    # Sending a POST request to the URL with the email parameter
    req = requests.post(url, data=value)

    # Printing the body of the response
    print(req.text)
