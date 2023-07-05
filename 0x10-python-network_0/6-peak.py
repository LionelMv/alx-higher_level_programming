# function that finds a peak in a list of integers

def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    peak = float("-inf")
    for num in list_of_integers:
        if num >= peak:
            peak = num
    return peak
