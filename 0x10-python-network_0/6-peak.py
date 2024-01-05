#!/usr/bin/python3
""" module with the findpeak function """


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers

    params:
        list_of_integers - unsorted list of integers
    """
    if not list_of_integers:
        return

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
