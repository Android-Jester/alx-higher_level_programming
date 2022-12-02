#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(sys.argv[1:])
    val = 0
    for i in range(argc + 1):
        val += int(sys.argv[i])
    print(f"{val:d}")
    
