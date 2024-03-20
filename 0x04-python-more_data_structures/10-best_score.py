#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        large = (None, None)
        for k, v in a_dictionary.items():
            if large[1] is None or v > large[1]:
                large = (k, v)
        return large[0]
