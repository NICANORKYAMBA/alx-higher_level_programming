#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    
    n1 = len(tuple_a)
    n2 = len(tuple_b)

    my_list = list(zip(tuple_a, tuple_b))
    n3 = len(my_list)

    for tup in my_list:
        if n1 < 2 and n2 < 2:
            my_list[1] = my_list[4] = 0
            total = 
        elif 
