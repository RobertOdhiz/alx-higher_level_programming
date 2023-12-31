#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = sys.argv[1:]
    args_len = len(args)
    operator = "+-*/"
    if args_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    b = int(args[2])
    a = int(args[0])
    if args[1] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif args[1] == "+":
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
        sys.exit(0)
    elif args[1] == "-":
        result = sub(a, b)
        print("{} - {} = {}".format(a, b, result))
        sys.exit(0)
    elif args[1] == "*":
        result = mul(a, b)
        print("{} * {} = {}".format(a, b, result))
        sys.exit(0)
    elif args[1] == "/":
        result = div(a, b)
        print("{} / {} = {}".format(a, b, result))
        sys.exit(0)
