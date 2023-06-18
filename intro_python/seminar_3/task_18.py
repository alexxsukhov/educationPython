"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""

array = []
count_elements = int(input("Введите количество элементов в массиве: "))

for i in range(count_elements):
    n = int(input("Введите элемент массива (число): "))
    array.append(n)

usr_number = int(input("Введите искомый элемент: "))

find_number = array[0]
difference = abs(find_number - usr_number)

for item in array:
    if item == usr_number:
        find_number = item
        break
    elif abs(item - usr_number) < difference:
        difference = abs(item - usr_number)
        find_number = item

print(f"Близкий элемент - {find_number}")
