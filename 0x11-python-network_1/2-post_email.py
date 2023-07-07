#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends POST req to URL, display response body utf-8
usage: ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""

from urllib import request, parse
from sys import argv


url = argv[1]
value = {
    "email": argv[2]
}

data = parse.urlencode(value)
data.encode("utf-8")
req = request.Request(url, data)
with request.urlopen(req) as response:
    print(response.read().decode("utf-8"))
