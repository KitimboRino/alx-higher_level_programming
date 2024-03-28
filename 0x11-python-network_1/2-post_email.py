#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    # Extracting URL and email from command line arguments
    url = argv[1]
    email = argv[2]

    # Encoding email parameter and creating request data
    value = {"email": email}
    data = urlencode(value).encode("ascii")

    # Creating request object with URL and data
    req = Request(url, data)

    # Sending the request and handling the response
    with urlopen(req) as response:
        # Decoding and printing the body of the response
        print(response.read().decode("utf-8", "replace"))
