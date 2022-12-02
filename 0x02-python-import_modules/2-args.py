#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    index = 1
    print(argv)
    if argc == 0:
        print(f"{argc} arguments.")
    elif argc == 1:
        print(f"{argc} argument:")
        print(f"{index:d}: {sys.argv[1]:s}")
    else:
        print(f"{argc:d} arguments:")
        while index <= argc:
            print(f"{index:d}: {sys.argv[index]:s}")
            index += 1
