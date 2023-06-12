#!/usr/bin/python3
for c in range(122, 96, -1):
    print("{}".format(chr(c).upper() if (122-c) % 2 != 0 else chr(c)), end="")
