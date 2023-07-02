"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

PATH_TO_FILE = "/home/alexxs/Documents/education/python/educationPython/immersion_in_python/seminar_5/text.txt"


def return_parse_path(path_to_file: str):
    *parts_path, full_name_file = path_to_file.split("/")
    absolute_path = "/".join(parts_path) + "/"
    name_file, expansion = map(str, full_name_file.split("."))
    return absolute_path, name_file, expansion


print(return_parse_path(PATH_TO_FILE))
