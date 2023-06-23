"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

DICT_FOR_HEX = {
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}

DIV_HEX = 16
END_CYCLE = 0

MAX_RANGE_HEX = 10

# number = int(input("Введите число для конвертации: "))
number = 1
res = ""

print(hex(number))

while number != END_CYCLE:
    remains = number % DIV_HEX
    if remains >= MAX_RANGE_HEX:
        res = res + DICT_FOR_HEX[remains]
    else:
        res = res + str(remains)

    number //= DIV_HEX


print(f"0x{res[::-1]}")
