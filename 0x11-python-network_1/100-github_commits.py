#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
(Interview question)
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
from sys import argv
import requests

if __name__ == "__main__":
    # Constructing URL based on provided repository name and owner
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    
    # Sending a GET request to retrieve commit information
    req = requests.get(url)
    
    # Extracting commits from the response
    commits = req.json()

    try:
        # Printing details of the first 10 commits
        for index in range(10):
            print("{}: {}".format(
                commits[index].get("sha"),
                commits[index].get("commit").get("author").get("name")))
    except IndexError:
        # Handling the case when there are fewer than 10 commits
        pass
