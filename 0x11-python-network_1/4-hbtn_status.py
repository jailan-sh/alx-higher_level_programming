#!/usr/bin/python3
""" POST an email """

if __name__ == "__main__":
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.content.decode("utf-8")))
