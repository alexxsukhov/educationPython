"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""

array = []
count_elements = int(input("Введите количество элементов в массиве: "))

for i in range(count_elements):
    n = int(input("Введите элемент массива (число): "))
    array.append(n)

usr_el = int(input("Введите искомый элемент: "))

count = 0
for item in array:
    if item == usr_el:
        count += 1
print(*array)
print(f"Искомый элемент встречается - {count} раз!")

