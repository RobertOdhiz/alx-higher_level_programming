#!/usr/bin/python3
import sys

args = sys.argv[1:]
args_len = len(args)
if args_len == 0:
    print("{} arguments.".format(args_len))
else:
    if args_len == 1:
        print("{} argument:".format(args_len))
    else:
        print("{} arguments:".format(args_len))
    for i in range(args_len):
        print("{}: {}".format(i + 1, args[i]))
