#!/usr/bin/python3
""" Initialiazing class MyList that inherits from list """


class MyList(list):
    """ Beginning of class definition """
    def print_sorted(self):
        """ Prints a sorted list """
        sorted_list = sorted(self)
        print(sorted_list)
