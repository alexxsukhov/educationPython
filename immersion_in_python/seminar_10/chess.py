class ChessQueens:
    CHECKERBOARD_SIZE = 8
    counter = 0

    def __init__(self, coordinate_list: list[tuple[int, int]]):
        self.coordinate_list = coordinate_list
        self.matrix = []

    def __gen_matrix_queens(self) -> list[list[int]]:
        """Генерация расположения ферзей в случайном порядке"""
        self.matrix = [[0 for _ in range(self.CHECKERBOARD_SIZE)] for _ in range(self.CHECKERBOARD_SIZE)]
        for row in self.coordinate_list:
            self.matrix[row[0]][row[1]] = 1

        return self.matrix

    def print_queens(self):
        """Вывод расположения ферзей на доске (визуальное представление)"""
        self.matrix = self.__gen_matrix_queens()
        for row in self.matrix:
            for item in row:
                if item == 1:
                    print("■", end=" ")
                else:
                    print("◘", end=" ")
            print()

    def check_chess_queen(self) -> bool:
        """Проверка бьют ли друг друга ферзи по координатам"""
        count_iter = len(self.coordinate_list)
        zip_coordinate = list(zip(*self.coordinate_list))
        check_result = True

        for i in range(count_iter):
            for j in range(i + 1, count_iter):
                if zip_coordinate[0][i] == zip_coordinate[0][j] or zip_coordinate[1][i] == zip_coordinate[1][j] or \
                        abs(zip_coordinate[0][i] - zip_coordinate[0][j]) == \
                        abs(zip_coordinate[1][i] - zip_coordinate[1][j]):
                    check_result = False
                    break

        return check_result


exm = ChessQueens([(1, 2), (3, 5), (3, 7), (5, 5), (2, 3), (4, 6)])

print(exm.check_chess_queen())
exm.print_queens()