#!/usr/bin/python3
""" What's my status? """


if __name__ == "__main__":
    import urllib.request
    from sys import argv
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        value = response.headers.get('X-Request-Id')
        print(value)
