#!/usr/bin/python3
""" POST an email """

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(mail)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
