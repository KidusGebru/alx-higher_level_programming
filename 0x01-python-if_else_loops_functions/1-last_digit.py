#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = f"{number % 10 if number > 0 else -1*((-1 * number) % 10)}"
if (int(last_digit) == 0):
    print(f"Last digit of {number} is {last_digit} and is 0")
elif (int(last_digit) > 5):
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")