#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    n = len(my_string)

    for character in range(0, n):
        if character != 'c' and character != 'C':
            newstring += my_string[character]
    return newstring
