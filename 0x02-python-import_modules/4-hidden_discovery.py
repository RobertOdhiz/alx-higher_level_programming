#!/usr/bin/python3
import py_compile
import hidden_4

if __name__ == "__main__":
    path = "hidden_4.pyc"
    names = [name for name in dir(hidden_4) if not name.startswith("__")]

    names.sort()

    for name in names:
        print("{}".format(name))
