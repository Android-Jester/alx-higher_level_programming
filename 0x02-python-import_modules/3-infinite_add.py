#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv, argc, val = sys.argv[1:], len(sys.argv[1:]), 0
    for i in range(argc):
        val += int(sys.argv[i])
    print(f"{val:d}")
    
