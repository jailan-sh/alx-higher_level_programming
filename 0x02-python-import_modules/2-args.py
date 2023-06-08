#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("0 arguments.")
    elif len(sys.argv) >= 2:
        print("{} arguments:".format(len(sys.argv)-1))
        argument = enumerate(sys.argv[1:], 1)
        for i, args in argument:
            print("{}: {}".format(i, args))


