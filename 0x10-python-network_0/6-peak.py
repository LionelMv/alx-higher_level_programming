#!/usr/bin/python3
"""
function that finds a peak in a list of integers
"""


def find_peak(list_of_integers):
    """
    Function to find the peak number
    """
    if list_of_integers == []:
        return None
    peak = list_of_integers[0]
    for num in list_of_integers:
        if num >= peak:
            peak = num
    return peak
