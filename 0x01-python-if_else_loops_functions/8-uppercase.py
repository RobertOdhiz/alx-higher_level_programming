#!/usr/bin/python3
def uppercase(str):
    final = ""
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        final += char
    print("{}".format(final))
