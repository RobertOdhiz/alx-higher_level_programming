#!/usr/bin/python3
#Finding the maximum value in a list
def max_integer(my_list=[]):
    if not my_list:
        return None
    #Set first value of list to maximum value
    maximum = my_list[0]
    #Iterating through the list
    for i in range(1, len(my_list)):
        #Check if the value at i is greater than the current maximum value and swap
        if my_list[i] > maximum:
            maximum = my_list[i]
    return (maximum)
