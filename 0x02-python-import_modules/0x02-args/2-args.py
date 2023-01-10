#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    arg_len = len(sys.argv) - 1 # its default value is 0 in this case
    list1 = sys.argv
    
    if arg_len == 0:
        print("{} arguments".format(arg_len))

    elif arg_len == 1:
        print("{} argument".format(arg_len))
        for i in range(1,len(list1)):
            print("{}: {}".format(i, list1[i]))

    else:
        print("{} arguments".format(arg_len))
        for i in range(1, len(list1)):
            print("{}: {}".format(i, list1[i]))    
