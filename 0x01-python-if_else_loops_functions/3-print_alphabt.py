#!/usr/bin/python3
for i in range(97, 97+26):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    print("{0}".format(chr(i)), end="")
