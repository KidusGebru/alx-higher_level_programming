#!/usr/bin/python3

sp = 0
for char in range(122, 96, -1):
    print("{}".format(chr(char - sp)), end="")
    if sp == 32:
        sp = 0
    else:
        sp = 32
