#!usr/bin/python3
def new_in_list(my_list, idx, element):

    newlist = my_list[:]
    n = len(my_list)

    for number in my_list:
        if idx < 0:
            return newlist
        elif idx > n:
            return newlist
        else:
            newlist[idx] = element
            return newlist
