#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    else:
        max_int = my_list[0]

        for i in range(len(my_list)):
            print("max_int = {}".format(max_int))
            if my_list[i] > max_int:
                max_int = my_list[i]

        return (max_int)
