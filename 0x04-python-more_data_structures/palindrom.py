#!/usr/bin/python3

n = 0
for a in range(9999, 9900, -1):
    for b in range(9999, 9900, -1):
        x = a * b
        s = str(x)
        if x > n:
            if s == s[::-1]:
                n = x
                print(n)
