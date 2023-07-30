class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                  range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError(
                "Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")
        result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*other.matrix)] for row in self.matrix]
        return Matrix(result)


# Создание матрицы
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Вывод на печать
print(matrix1)
print(matrix2)

# Сравнение
print(matrix1 == matrix2)

# Сложение
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Умножение
matrix_product = matrix1 * matrix2
print(matrix_product)