# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
def usr_exp(a, b):
    if b == 1:
        return a
    else:
        return a * usr_exp(a, b - 1)


usr_number = int(input("Введите число: "))
exp = int(input("Введите степень числа: "))


print(usr_exp(usr_number, exp))
