#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    number = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int and number != x:
                print('{:d}'.format(my_list[i]), end='')
                number += 1
        except TypeError:
            continue

    print()

    return number
