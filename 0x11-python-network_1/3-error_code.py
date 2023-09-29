#!/usr/bin/python3
""" POST an email """

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8').code
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
