"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction


def summary_fractions(first_fraction, second_fraction) -> str:
    first_fraction_list = first_fraction.split("/")
    second_fraction_list = second_fraction.split("/")

    first_number_numerator = int(first_fraction_list[0])
    first_number_denominator = int(first_fraction_list[1])

    second_number_numerator = int(second_fraction_list[0])
    second_number_denominator = int(second_fraction_list[1])

    common_denominator = None
    if first_number_denominator % second_number_denominator == 0:
        common_denominator = first_number_denominator
    elif second_number_denominator % first_number_denominator == 0:
        common_denominator = second_number_denominator
    else:
        common_denominator = int(first_fraction_list[1]) * int(second_fraction_list[1])

    first_multiplier = int(common_denominator / first_number_denominator)
    second_mmultiplier = int(common_denominator / second_number_denominator)

    common_numerator = first_number_numerator * first_multiplier + \
                       second_number_numerator * second_mmultiplier

    return f"{common_numerator}/{common_denominator}"


def multiply_fractions(first_fraction, second_fraction) -> str:
    first_fraction_list = first_fraction.split("/")
    second_fraction_list = second_fraction.split("/")

    first_number_numerator = int(first_fraction_list[0])
    first_number_denominator = int(first_fraction_list[1])

    second_number_numerator = int(second_fraction_list[0])
    second_number_denominator = int(second_fraction_list[1])

    common_numerator = first_number_numerator * second_number_numerator
    common_denominator = first_number_denominator * second_number_denominator
    common_divider = 1

    for i in range(2, common_denominator // 2):
        if common_numerator % i == 0 and common_denominator % i == 0:
            common_divider = i

    if common_divider > 1:
        common_numerator //= common_divider
        common_denominator //= common_divider

    return f"{common_numerator}/{common_denominator}"


usr_first_fraction = input("Введите первую дробь: ")
usr_second_fraction = input("Введите вторую дробь: ")

print("Вывод с помощью модуля")
print(Fraction(usr_first_fraction) + Fraction(usr_second_fraction))
print(Fraction(usr_first_fraction) * Fraction(usr_second_fraction))

print()

print("Вывод с помощью пользовательских функций")
print(summary_fractions(usr_first_fraction, usr_second_fraction))
print(multiply_fractions(usr_first_fraction, usr_second_fraction))
