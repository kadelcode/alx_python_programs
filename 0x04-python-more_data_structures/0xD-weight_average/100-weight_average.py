#!/usr/bin/python3
def weight_average(my_list=[]):
    tuple_sum = 0
    last_num_sum = 0

    for i in my_list:
        mul = i[0] * i[len(i) - 1] # multiply each element in tuple
        tuple_sum += mul
        last_num_sum += i[len(i) - 1]

    average = tuple_sum / last_num_sum

    return (average)
