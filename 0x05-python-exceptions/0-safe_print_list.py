#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    while idx < x:
        try:
            print(my_list[idx], end="")
        except IndexError:
            break
        idx += 1
    print()
    return idx

# my_list = [1, 2, 3, 4, 5]
# nb_print = safe_print_list(my_list, 2)
# print("nb_print: {:d}".format(nb_print))

# nb_print = safe_print_list(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))

# nb_print = safe_print_list(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))
