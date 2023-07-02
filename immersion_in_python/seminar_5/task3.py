"""
Создайте функцию генератор чисел Фибоначчи
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
"""

N = 10  # задаем количество элементов последовательности


def gen_fibo(n: int):
    current_number = end_number = 1
    yield current_number
    yield end_number

    for _ in range(n - 2):
        res = current_number + end_number
        current_number = end_number
        end_number = res

        yield res


for i in gen_fibo(N):
    print(i, end=" ")
