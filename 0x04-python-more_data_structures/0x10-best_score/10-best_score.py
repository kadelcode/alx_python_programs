#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return (None)

    score_list = []
    for i in a_dictionary:
        score_list.append(a_dictionary[i])
    max_score = max(score_list)

    for i in a_dictionary:
        if a_dictionary[i] == max_score:
            return (i)
