#!/usr/bin/python3
"""A Script takes a url and email sends a POST request with the
Email as parameter and diplays a response body
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
