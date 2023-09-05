#!/usr/bin/python3
for first in range(10):
    for second in range(first + 1, 10):
        num = "{}{}".format(first, second)
        print(num, end=", " if int(num) < 89 else '\n')
