"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
number = randint(LOWER_LIMIT, UPPER_LIMIT)
COUNT_ATTEMPS = 10

iterator = 1

while iterator <= COUNT_ATTEMPS:
    print(f"Попытка {iterator}")
    usr_number = int(input("Введите число: "))
    iterator += 1
    if usr_number > number:
        print("Число меньше")

    elif usr_number < number:
        print("Число больше")
    else:
        print(f"Вы угдали, загаданное число - {usr_number}")
        break

else:
    print(f"Попытки закончились. Загаданное число {number}")
