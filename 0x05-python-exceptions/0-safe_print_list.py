#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print("")
        return x
    except(IndexError):
        for i in my_list:
            print("{}".format(i))
        return len(my_list)

