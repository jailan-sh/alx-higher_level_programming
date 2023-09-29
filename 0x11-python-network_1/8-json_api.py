#!/usr/bin/python3
""" Search API """

if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) == 1:
        pyload = {'q': ""}
    else:
        payload = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        r_dict = r.json()
        if r_dict = {}:
            print("No result")
        else:
            print("[{}] {}".format(r_dict[id], r_dict[name])
    except ValueError:
        print("Not a valid JSON")
