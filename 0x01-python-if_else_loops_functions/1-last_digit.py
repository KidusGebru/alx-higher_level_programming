#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = f"{number % 10 if number > 0 else -1*((-1 * number) % 10)}"
if (int(ld) == 0):
    print(f"Last digit of {number} is {ld} and is 0")
elif (int(ld) > 5):
    print(f"Last digit of {number} is {ld} and is greater than 5")
else:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
