#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This function takes two numbers as input parameters and returns their sum.
    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added. Default is 98.

    Returns:
        An int of sum of a and b

    Raises:
        TypeError: If either of `a` or `b` is not an integer or a float.
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


# print(add_integer(1, 2))
# print(add_integer(100, -2))
# print(add_integer(2))
# print(add_integer(100.3, -2))
# try:
#     print(add_integer(4, "School"))
# except Exception as e:
#     print(e)
# try:
#     print(add_integer(None))
# except Exception as e:
#     print(e)
