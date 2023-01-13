#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict_list = []

    for i in a_dictionary:
        sort_dict_list.append(i)

    sorted_dicts = sorted(sort_dict_list)

    for i in sorted_dicts:
        print("{}: {}".format(i, a_dictionary[i]))
