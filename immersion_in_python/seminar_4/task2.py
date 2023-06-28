"""
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента.
(речь идет про **kwargs)
"""


def return_dictionary_from_kwargs(**kwargs):
    return kwargs


print(return_dictionary_from_kwargs(key=0, key_2=1, key_3=3))
