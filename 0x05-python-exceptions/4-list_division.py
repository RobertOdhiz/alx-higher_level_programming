#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    try:
        for i in range(list_length):
            try:
                el_1 = my_list_1[i] if i < len(my_list_1) else 0
                el_2 = my_list_2[i] if i < len(my_list_2) else 0
                if not isinstance(el_1, (int, float)) or \
                   not isinstance(el_2, (int, float)):
                    raise TypeError("wrong type")
                if el_2 == 0:
                    raise ZeroDivisionError("division by 0")
                quotient = el_1 / el_2
                res_list.append(quotient)
            except TypeError:
                res_list.append("wrong type")
            except ZeroDivisionError:
                res_list.append("division by 0")
    except IndexError:
        res_list.append("out of range")
    finally:
        return res_list
