#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{}".format(chr(i - (0 if i % 2 == 0 else 32))), end="")
