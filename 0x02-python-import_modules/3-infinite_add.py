#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    args_len = len(args)
    sum = 0
    for i in range(args_len):
        sum += int(args[i])
    print("{}".format(sum))
