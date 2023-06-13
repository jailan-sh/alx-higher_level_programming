#!/usr/bin/env python3
def remove_char_at(str, n):
    if n > len(str) - 1 or n < ((len(str) -1) * -1):
        return (str)
    else:
        newstr = str.replace(str[n], "")
        return (newstr)
