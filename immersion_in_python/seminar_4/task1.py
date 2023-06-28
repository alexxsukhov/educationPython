"""
Напишите функцию для транспонирования матрицы
Пример:
[[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
"""


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()


def transposition_matrix(matrix):
    new_matrix = [[0 for j in range(len(usr_list))] for i in range(len(usr_list[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix


usr_list = [
    [1, 2, 3],
    [4, 5, 6]
]

print_matrix(usr_list)
print(usr_list, end="\n\n")

print_matrix(transposition_matrix(usr_list))
print(transposition_matrix(usr_list), end="\n\n")
