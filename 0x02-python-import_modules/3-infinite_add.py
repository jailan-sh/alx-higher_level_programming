#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0")
    elif argc >= 1:
        argv_sum = sum(int(arg) for arg in sys.argv[1:])
        print("{:d}".format(argv_sum))
