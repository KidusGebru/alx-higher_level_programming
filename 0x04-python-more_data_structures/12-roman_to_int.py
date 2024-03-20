#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        n = 0
        index = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        for i in range(len(roman_string)):
            if index.get(roman_string[i], 0) == 0:
                return 0
            if i != (len(roman_string) - 1) and \
                    index[roman_string[i]] < index[roman_string[i + 1]]:
                n += index[roman_string[i]] * -1
            n += index[roman_string[i]]
        return n
