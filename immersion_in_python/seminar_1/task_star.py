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
print(number)
usr_number = (LOWER_LIMIT + UPPER_LIMIT) // 2

i = 1

while True:
    print(f"Попытка {i}")
    i += 1
    if usr_number > number:
        print("Число меньше")
        UPPER_LIMIT = usr_number

    elif usr_number < number:
        print("Число больше")
        LOWER_LIMIT = usr_number
    else:
        print(usr_number)
        print()
        break
    usr_number = (LOWER_LIMIT + UPPER_LIMIT) // 2

