#!/usr/bin/python3
"""
A Script takes urrl sends a request too the url and displays
The value "X-Request-ID" in the header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
