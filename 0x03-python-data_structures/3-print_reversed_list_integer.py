#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = []

    for element in my_list:
        rev_list.insert(0, element)
    for number in rev_list:
        print("{}".format(number))
