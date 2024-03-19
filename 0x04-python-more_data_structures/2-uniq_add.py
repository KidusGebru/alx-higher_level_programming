#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = []
    for x in my_list:
        if uniq.count(x) == 0:
            uniq.append(x)
    return sum(uniq)
