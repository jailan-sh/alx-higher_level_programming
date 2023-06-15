#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = len(roman_string)
        n = i - 1
        num = 0
        while n >= 0:
            if n < i-1 and dic[roman_string[n]] < dic[roman_string[n + 1]]:
                num -= dic[roman_string[n]]
            else:
                num += dic[roman_string[n]]
            n -= 1
        return num
    elif roman_string is None or not isinstance(roman_string, str):
        return 0
