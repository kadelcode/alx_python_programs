#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary:
        if key in a_dictionary:
            a_dictionary[key] = value
            return (a_dictionary)
        else:
            a_dictionary[key] = value
            return (a_dictionary)
