#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print(f"{i:d}{j:d}", end="")
            if i < 8:
                print(", ", end="")
