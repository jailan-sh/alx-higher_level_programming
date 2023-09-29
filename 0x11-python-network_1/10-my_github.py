#!/usr/bin/python3
"""My GitHub!"""

if __name__ == "__main__":
    import requests
    import sys
    payload = {'username': sys.argv[1], 'password': sys.argv[2]}
    r = requests.get('https://docs.github.com/en/rest/users', data=payload)
    r_dict = r.json()
    if r_dict == {}:
        print("None")
    else:
        print(r_dict['id'])

