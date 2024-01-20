def sum_list_recursivelly(list):
    if len(list) == 0:
        return 0
    else:
        first_item = list.pop(0)
        return first_item + sum_list_recursivelly(list)


print(sum_list_recursivelly([3, 5, 7, 8]))
