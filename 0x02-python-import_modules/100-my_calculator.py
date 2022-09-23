#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    
    """
    Handles basic operations

    Performs basic operations like addition, substraction,
    multiplication and division between two numbers.

    The program will execute an operation between two numbers
    selected by the operator sent to the program.
    """

    l_av = len(sys.argv) - 1
    
    if l_av == 3:
        operator = sys.argv[2]
        num_a = int(sys.argv[1])
        num_b = int(sys.argv[3])
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
        elif operator != '+' and operator != '-' and operator != '*' and operator != '/':
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
