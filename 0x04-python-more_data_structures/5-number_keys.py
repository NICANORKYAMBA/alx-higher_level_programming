#!/usr/bin/python3

def number_keys(a_dictionary):

    total = 0

    for keys in range(len(a_dictionary.keys())):
        total = total + keys
    return total
