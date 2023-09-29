#!/usr/bin/python3
"""My GitHub!"""

if __name__ == "__main__":
    import requests
    import sys
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    r_dict = r.json()
    if r_dict == {}:
        print("None")
    else:
        print(r_dict.get('id'))
