#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sum = 0
    arg_lists = sys.argv

    for i in range(1, len(arg_lists)):
        sum = sum + int(arg_lists[i])
    print(sum)
