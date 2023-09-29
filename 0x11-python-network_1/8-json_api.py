#!/usr/bin/python3
""" Search API """

if __name__ == "__main__":
    import requests
    import sys
    if len(sys.args) == 1:
        pyload = {'q': ""}
    else:
        payload = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    data_dic = r.json()
    print("[{}] {}".format(data_dic[id], data_dic[name])
