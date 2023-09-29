#!/usr/bin/python3
"""displays the body of the response."""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    print(r)
    print("Error code: {}".format())
