#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    adding = add(a, b)
    diff = sub(a, b)
    prod = mul(a, b)
    quot = div(a, b)
    print("{} + {} = {}".format(a, b, adding))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, prod))
    print("{} / {} = {}".format(a, b, quot))
