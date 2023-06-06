#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if num < 6 and num != 0 and number > 0:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
elif num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif number < 0 and num != 0:
    print(f"Last digit of {number} is -{num} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {num} and is 0")
