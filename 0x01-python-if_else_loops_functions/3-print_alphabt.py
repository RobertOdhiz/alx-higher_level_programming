#!/usr/bin/python3
for i in range(97, 123):
    ch = chr(i)
    if ch != 'q' and ch != 'e':
        print("{0}".format(ch), end="")
