"""
1.Решить задачи, которые не успели решить на семинаре:
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
"""
MIN_RANGE = 2
MAX_RANGE = 10
PLUS_ONE_STEP = 1

for i in range(MIN_RANGE, MAX_RANGE):
    for j in range(MIN_RANGE, MAX_RANGE + PLUS_ONE_STEP):
        print(f"{i} x {j} = {i * j}")
    print()