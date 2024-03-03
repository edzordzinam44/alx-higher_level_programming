#!/usr/bin/python3
"""A Script takes Github credentials and uses "Github API"
To display your "ID"
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasic(sys.argv[1], sys.argv[1])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
