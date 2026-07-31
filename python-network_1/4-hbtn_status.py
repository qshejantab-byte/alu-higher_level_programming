#!/usr/bin/python3
"""Script that fetches the status using requests."""
import requests

if __name__ == "__main__":
    r = requests.get("https://alu-intranet.hbtn.io/status")
    body = r.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
