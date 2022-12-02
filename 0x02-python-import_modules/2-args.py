#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv) + 1
    if argc == 0:
        print(f"{argc:d} arguments.")
    elif argc == 1:
        print(f"{argc:d} argument:")
        print(f"{1}: {sys.argv[1]}")
    else:
        print(f"{argc:d} arguments:")
    for i in range(argc):
        print(f"{i+1:d}: {sys.argv[i]:s}")
