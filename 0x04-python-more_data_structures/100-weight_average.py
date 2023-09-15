#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = 0
    denominator = 0
    for tuple_val in my_list:
        numerator += tuple_val[0] * tuple_val[1]

    for tup in my_list:
        denominator += tup[1]

    result = numerator / denominator

    return result
