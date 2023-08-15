import doctest
from main import Rectangle
import random

TRUE_SQUARE = 20
RANDOM_SQUARE = 19  # random.randint(10, 40)


def check_width(first: int or float, second: int or float) -> bool:
    """
    Проверка двух прямоугольников на квадрат
    # Проверка ширины, вернет истину
    >>> check_width(Rectangle(2, 2).width, Rectangle(2, 2).width)
    True
    """
    first = Rectangle(2, 2)
    second = Rectangle(2, 2)
    if first.width == second.width:
        return True


def check_value(square: int) -> bool:
    '''
    #Сравнение площади заданного прямоугольника со случайным числом
    >>> check_value(TRUE_SQUARE)
    True
    '''
    rect_square = Rectangle(4, 5).square()

    if rect_square == TRUE_SQUARE:
        return True
    else:
        raise ValueError("Не совпало!")


if __name__ == '__main__':
    doctest.testmod(verbose=True)

    # ValueError: Try again
    # >>>check_value(RANDOM_SQUARE)
    # "Не совпало!"