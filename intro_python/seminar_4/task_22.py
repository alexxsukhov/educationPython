lst_1 = [30, 6, 6, 5, 4, 4, 5, 5, 6, 6, 7, 7]
lst_2 = [15, 12, 26, 25, 14, 24]
lst = (lst_1 + lst_2)
lst_set = set(lst)
lst_sort = sorted(list(lst_set))

print(*lst_sort)
