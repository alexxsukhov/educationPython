# Задача 2: Найдите сумму цифр трехзначного числа.#
# *Пример:*#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


number = int(input('Введите число: '))
summary = 0

while number > 0:
    item = number % 10
    number = number // 10
    summary = summary + item

print(f'Сумма составляющих трехзначного числа: {summary}')

