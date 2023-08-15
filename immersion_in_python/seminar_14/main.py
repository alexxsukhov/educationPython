import unittest


class Rectangle:
    """Класс для создания прямоугольников с заданием сторон, нахождения
    периметра, площади и их сравнения
    """

    def __init__(self, length: float, width: float or None = None) -> None:
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def per(self) -> float:
        return self.length * 2 + self.width * 2

    def square(self) -> float:
        return self.length * self.width

    def __add__(self, other) -> float or int:
        sum_of_per = self.per() + other.per()
        width_rect_c = self.width
        length_rect_c = sum_of_per / 2 - width_rect_c

        return Rectangle(width_rect_c, length_rect_c)

    def __sub__(self, other):
        min_of_per = abs(self.per() - other.per())
        width_rec_c = min(self.width, other.width, self.length, other.length)
        length_rec_c = min_of_per / 2 - width_rec_c
        return Rectangle(width_rec_c, length_rec_c)

    def __eq__(self, other):
        return self.square() == other.square()

    def __ne__(self, other):
        return self.square() != other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.square() <= other.square()


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rec1 = Rectangle(2, 4)
        self.rec2 = Rectangle(3, 5)
        self.rec3 = Rectangle(4, 5)

    def test_sum_perimetr(self):
        self.assertEqual(Rectangle(3, 8), self.rec2 + self.rec3)

    def test_calc_area(self):
        self.assertEqual(3, self.rec2.square(), 'проверьте заданную площадь ')

    def test_equal_recs(self):
        self.assertFalse(self.rec1 == self.rec2)


if __name__ == '__main__':
    unittest.main()
