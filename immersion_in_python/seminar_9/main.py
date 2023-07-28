"""
Напишите следующие функции:
* Нахождение корней квадратного уравнения
* Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
* Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
* Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
import csv
import json
from random import randint

START_RANDOM_RANGE = 1
STOP_RANDOM_RANGE = 50
COUNT_NUMBERS = 3


def generate_random_numbers_csv(file_path: str, num_rows: int) -> None:
    """Функция генерации случайных чисел с записью в cvs файл"""
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE) for _ in range(COUNT_NUMBERS)]
            csv_writer.writerow(row)


def save_to_json(func):
    """Функция сохранение работы функции в json файл"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("results.json", "w") as jsonfile:
            json.dump({"results": result}, jsonfile, indent=4)

        return result
    return wrapper


def quadratic_equation(a: int | float, b: int | float, c: int | float) -> tuple[float | int, float | int]:
    """Функция нахождения корней квадратного уравнения"""
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)

    return str(x1), str(x2)


@save_to_json
def reading_csv_in_data(file_path: str) -> dict[str, tuple[int | float, int | float]]:
    results = {}
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            try:
                a, b, c = map(float, row)
                roots = quadratic_equation(a, b, c)
                results[f"{a}, {b}, {c}"] = roots
            except ValueError:
                print("Invalid input. Skipping row:", row)

    return results


f_path = "numbers.csv"
num_rows = 100
generate_random_numbers_csv(f_path, num_rows)
reading_csv_in_data(f_path)
