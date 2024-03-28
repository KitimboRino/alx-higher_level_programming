#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    # Create a Request object with the URL
    req = Request("https://alx-intranet.hbtn.io/status")

    # Open the request using urlopen
    with urlopen(req) as response:
        # Read the response body
        body = response.read()

        # Print out the body response
        print("Body response:")
        # Print the type of the body
        print("\t- type: {}".format(type(body)))
        # Print the content of the body
        print("\t- content: {}".format(body))
        # Print the UTF-8 decoded content of the body
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
