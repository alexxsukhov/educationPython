"""Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь."""

from random import randint

COUNT_QUEEN = 8
CHECKERBOARD_SIZE = 8


# coord_list =
# [list(map(int, input("Введите расположение ферзя (через пробел): ").split())) for _ in range(COUNT_QUEEN)]


def check_chess_queen(queen_list_coordinates: list[tuple[int, int]]) -> bool:
    """Проверка бьют ли друг друга ферзи по координатам"""
    count_iter = len(queen_list_coordinates)
    zip_coordinate = list(zip(*queen_list_coordinates))

    check_result = True

    for i in range(count_iter):
        for j in range(count_iter):
            if i == j:
                continue
            elif zip_coordinate[0][i] == zip_coordinate[0][j] or zip_coordinate[1][i] == zip_coordinate[1][j] or \
                    abs(zip_coordinate[0][i] - zip_coordinate[0][j]) == \
                    abs(zip_coordinate[1][i] - zip_coordinate[1][j]):
                check_result = False
                break
            else:
                check_result = True

    return check_result


def gen_list_coordinates(count_queens: int):
    """Генерация списка координат ферзей"""
    coordinate_list = []

    counter = 0

    while counter < 8:
        x = randint(0, 7)
        y = randint(0, 7)
        if (x, y) not in coordinate_list:
            coordinate_list.append((x, y))
            counter += 1

    return coordinate_list


def gen_matrix_queens(coordinates: list[tuple[int, int]]) -> list[list[int]]:
    """Генерация расположения ферзей в случайном порядке"""
    matrix = [[0 for _ in range(CHECKERBOARD_SIZE)] for _ in range(CHECKERBOARD_SIZE)]

    for row in coordinates:
        matrix[row[0]][row[1]] = 1

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print()


def print_queens(matrix):
    for row in matrix:
        for item in row:
            if item == 1:
                print("■", end=" ")
            else:
                print("◘", end=" ")
        print()


if __name__ == '__main__':
    list_coord = gen_list_coordinates(COUNT_QUEEN)
    matrix_queens = gen_matrix_queens(list_coord)
    print_queens(matrix_queens)
    print(check_chess_queen(list_coord))
