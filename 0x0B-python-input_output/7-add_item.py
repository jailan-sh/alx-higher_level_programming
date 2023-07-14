#!/usr/bin/python3
""" Load, add, save """

import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

if os.path.isfile(filename):
    nlist = load_from_json_file(filename)
else:
    nlist = []

for i in range(1, len(sys.argv)):
    nlist.append(sys.argv[i])

save_to_json_file(nlist, filename)
