# Задача 7.
# Создайте модуль и напишите в нём функцию,
# которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

from sys import argv

__all__ = ['check_date_function']

_LEAP = 4
_END_DAY = 31
_START_DAY = 1
_END_MONTH = 12
_START_MONTH = 1
_END_YEAR = 9999
_START_YEAR = 1


def check_date_function(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    return ((_END_DAY >= day >= _START_DAY) and
            (_END_MONTH >= month >= _START_MONTH) and
            (_END_YEAR >= year >= _START_YEAR))


def _is_leap_year(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if year % _LEAP == 0:
        return True
    return False


if __name__ == '__main__':
    DATE_FROM_CONSOLE = argv[1]
    print(check_date_function(DATE_FROM_CONSOLE))
    print(_is_leap_year(DATE_FROM_CONSOLE))

