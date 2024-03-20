#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    wa = [0, 0]
    for t in my_list:
        wa[0] += t[0] * t[1]
        wa[1] += t[1]
    return wa[0] / wa[1]
