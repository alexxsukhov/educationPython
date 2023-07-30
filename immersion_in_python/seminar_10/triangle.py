class Triangle:
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def is_exists(self):
        if self.side_a + self.side_b > self.side_c and \
                self.side_b + self.side_c > self.side_a and \
                self.side_c + self.side_a > self.side_b:
            return True
        return False

    def form_triangle(self):
        if self.side_a == self.side_b == self.side_c:
            return "Треугольник равносторонний"
        elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_c == self.side_a:
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"


usr_triangle = Triangle(10, 10, 12)
print(usr_triangle.is_exists())
print(usr_triangle.form_triangle())
