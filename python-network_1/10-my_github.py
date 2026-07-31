#!/usr/bin/python3
"""Script that displays your GitHub id using Basic Authentication."""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, password))
    print(r.json().get("id"))
