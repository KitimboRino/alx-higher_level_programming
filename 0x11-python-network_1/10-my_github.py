#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Extracting GitHub username and password from command line arguments
    username = argv[1]
    password = argv[2]

    # Creating authentication object with Basic Authentication
    auth = HTTPBasicAuth(username, password)

    # Sending a GET request to retrieve user information
    req = requests.get("https://api.github.com/user", auth=auth)

    # Printing the user ID
    print(req.json().get("id"))
