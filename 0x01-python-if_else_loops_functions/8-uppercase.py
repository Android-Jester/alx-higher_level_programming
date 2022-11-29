#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= 97) or (ord(i) < (97+26)):
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print(i, end="")
    print("\n")
