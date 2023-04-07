#!/usr/bin/python3
"""
Module 4-print_square
Function prints a square of "#"s.
"""


def print_square(size):
    """Prints a square of '#'s."""
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
