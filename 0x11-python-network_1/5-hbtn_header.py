#!/usr/bin/python3
""" header """

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    value = r.headers.get("X-Request-Id")
    print(value)
