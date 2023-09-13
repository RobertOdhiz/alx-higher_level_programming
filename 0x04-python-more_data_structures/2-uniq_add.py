#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    add = 0
    list_len = len(my_list)
    for num in my_list:
        if num not in unique:
                add += num
                unique.add(num)

    return add
