#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    # Sending a GET request to the specified URL
    req = requests.get("https://alx-intranet.hbtn.io/status")

    # Printing response information
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
