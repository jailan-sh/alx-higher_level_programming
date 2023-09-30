#!/usr/bin/python3
"""My GitHub!"""

if __name__ == "__main__":
    import requests
    import sys
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[1], sys.argv[2]))
    r_dict = r.json()
    for k in r_dict[:10]:
        print("{}: {}".format(k.get('sha'),
                              k.get('commit').get('author').get('name')))
