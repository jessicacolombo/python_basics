import math


def sum_list(list):
    if len(list) == 0:
        return 0
    else:
        first_item = list.pop(0)
        return first_item + sum_list(list)


def count_list_length(list):
    if len(list) == 0:
        return 0
    else:
        list.pop(-1)
        return 1 + count_list_length(list)


def get_highest_value(list, highest=0):
    if len(list) == 0:
        return highest
    else:
        popped = list.pop(0)
        if popped > highest:
            return get_highest_value(list, popped)

        return get_highest_value(list, highest)


def binary_search(list, searched_item):
    mid = (len(list) - 1) // 2
    mid_val = list[mid]
    # print({"lista": list, "meio": mid,"meio_val": mid_val,"searched": searched_item,"condition": mid_val == searched_item})

    if mid_val == searched_item:
        return searched_item
    elif mid_val > searched_item and len(list) > 1:
        binary_search(list[:mid], searched_item)
    elif mid_val < searched_item and len(list) > 1:
        binary_search(list[(mid + 1) :], searched_item)
    else:
        return False
