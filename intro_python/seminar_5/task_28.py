# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. И
# з всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4
def usr_summary(a, b):
    if a == 0:
        return b
    return usr_summary(a - 1, b + 1)


firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))


print(usr_summary(firstNumber, secondNumber))
