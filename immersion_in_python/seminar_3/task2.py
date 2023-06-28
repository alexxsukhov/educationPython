"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
Пример:
[1, 2, 3, 1, 2, 4, 5] -> [1, 2]
"""

usr_list = [1, 2, 3, 1, 2, 4, 5, 5, 5, 4, 4, 7, 8, 9]
double_element_list = []

for item in usr_list:
    if item not in double_element_list and usr_list.count(item) >= 2:
        double_element_list.append(item)

print(double_element_list)
