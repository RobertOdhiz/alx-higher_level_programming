#!/usr/bin/python3
def multiply_by_number(x, number):
    return x * number

def multiply_list_map(my_list, number):
    result = list(map(multiply_by_number, my_list, [number] * len(my_list)))
    return result
