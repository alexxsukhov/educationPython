from random import randint

length_array = int(input("Введите количество элементов массива: "))

min_value = int(input("Введите порог генерации элементов от: "))
max_value = int(input("Введите порог генерации элементов от: "))

min_range = int(input("Введите минимальный порог искомых элементов: "))
max_range = int(input("Введите максимальный порог искомых элементов: "))

array = [randint(min_value, max_value) for i in range(length_array)]

array_index = [i for i in range(len(array)) if min_range < array[i] < max_range]

print()
print(array)
print()
print(array_index)
