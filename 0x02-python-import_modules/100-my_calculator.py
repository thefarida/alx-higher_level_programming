#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    """This program executes an operation between two numbers and a selected operator"""

    l_av = len(argv) - 1
    
    if l_av == 3:
        operator = argv[2]
        num_a = int(argv[1])
        num_b = int(argv[3])
        if operator == '+':
            res = add(num_a, num_b)
            print('{:d} + {:d} = {:d}'.format(num_a, num_b, res))
        elif operator == '-':
            res = sub(num_a, num_b)
            print('{:d} - {:d} = {:d}'.format(num_a, num_b, res))
        elif operator == '*':
            res = mul(num_a, num_b)
            print('{:d} * {:d} = {:d}'.format(num_a, num_b, res))
        elif operator == '/':
            res = div(num_a, num_b)
            print('{:d} / {:d} = {:d}'.format(num_a, num_b, res))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
