#!/usr/bin/python3
"""A Script that takes url and sends a url request and displays the value of the
X-Request-Id varuable found in the header
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
