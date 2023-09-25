#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for val in my_list:
        if count < x:
            try:
                print("{}".format(val), end="")
                count += 1
            except TypeError:
                pass
    print("")
    return count
