#!/usr/bin/python3
"""
given URL & email as params, display response body utf-8, print error codes
usage: ./7-error_code.py http://0.0.0.0:5000/status_401
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
