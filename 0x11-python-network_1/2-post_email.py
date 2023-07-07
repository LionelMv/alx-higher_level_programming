#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
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
