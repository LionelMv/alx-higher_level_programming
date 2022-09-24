#!/usr/bin/python3
for letter in range(ord("z"), ord("a") - 1, -2):
    print("{:c}{:s}".format(letter, chr(letter - 33)), end="")
