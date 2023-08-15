from main import Rectangle
import pytest


def test_perimeter_calculation():
    rectangle = Rectangle(4, 6)
    assert rectangle.per() == 20


def test_square_calculation():
    rectangle = Rectangle(4, 6)
    assert rectangle.square() == 24


def test_rectangle_addition():
    rectangle1 = Rectangle(4, 6)
    rectangle2 = Rectangle(3, 5)
    new_rectangle = rectangle1 + rectangle2
    assert new_rectangle.length == 4  # Ожидаемый результат: (4 + 3) / 2 = 3.5
    assert new_rectangle.width == 3.5  # Ожидаемый результат: (20 + 10) / 2 - 3.5 = 3.5


def test_rectangle_subtraction():
    rectangle1 = Rectangle(8, 10)
    rectangle2 = Rectangle(3, 5)
    new_rectangle = rectangle1 - rectangle2
    assert new_rectangle.length == 5  # Ожидаемый результат: (18 - 10) / 2 = 4
    assert new_rectangle.width == 4  # Ожидаемый результат: (8 - 3) / 2 = 2.5


def test_rectangle_comparison():
    rectangle1 = Rectangle(4, 6)
    rectangle2 = Rectangle(3, 5)
    assert rectangle1 > rectangle2
    assert rectangle1 >= rectangle2
    assert rectangle2 < rectangle1
    assert rectangle2 <= rectangle1
    assert rectangle1 != rectangle2


if __name__ == '__main__':
    pass
