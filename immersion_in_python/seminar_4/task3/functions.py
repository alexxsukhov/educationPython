from config import *


def replenishment(remains: int) -> int:
    """Функция пополнения лицевого счета"""
    income = int(input("Введите сумму для пополнения: "))
    if income % MONEY_DIV == 0:
        remains += income
    else:
        print('incorrect summ')

    return remains


def withdrawal(remains: int) -> int:
    """Функция снятия с лицевого счета"""
    outcome = int(input("Введите сумму для снятия: "))

    commission = remains * TAX_OUTCOME
    if commission >= MAX_TAX_OUT:
        commission = MAX_TAX_OUT
    elif commission <= MIN_TAX_OUT:
        commission = MIN_TAX_OUT

    if outcome % MONEY_DIV == 0 and commission < remains:
        remains -= commission
        remains -= outcome
    else:
        print('Некорректная сумма')

    return remains


def bonus_tax(remains: int, count_operation: int) -> int:
    """Функция изменения лицевого счета налог и бонус"""
    if remains >= LUXURY_LIMIT:
        remains *= TAX_LUXURY
        print('Раскулачивание')
    if count_operation % OPERATIONS_FOR_BONUS == 0 and count_operation != 0:
        remains *= BONUS_FOR_OPERATION
        print('Бонус за 3 операции')

    return remains


def main(remains: int, count_operation: int = 0):
    """Главная функция"""
    while True:
        remains = bonus_tax(remains, count_operation)
        choose = input(f"{MODES}")

        match choose:
            case "1":
                remains = replenishment(remains)
                count_operation += 1
            case "2":
                remains = withdrawal(remains)
                count_operation += 1
            case "3":
                print("До встречи!")
                break
            case _:
                print(f'Некорректное действие')

        print(f'Текущий баланс: {remains}')
