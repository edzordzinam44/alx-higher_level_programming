#!/usr/bin/python3
"""A Script takes url sends a request to url and displays the
body response decoded as (utf-8)
    -Must handle HTTP errors
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
