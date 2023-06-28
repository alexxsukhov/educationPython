"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
Верните все возможные варианты комплектации рюкзака.
"""
import random

MAX_LOAD = 20

things_dict = {
    "вода": 10,
    "коньячок": 2,
    "шашлычок": 5,
    "картошечка": 5,
    "пивасик": 13,
    "овощи(огурка, помидорка)": 5,
}
variables_things_dict = {}
things_list = []
common_mass = 0

while common_mass <= MAX_LOAD:
    k = random.choice(list(things_dict.keys()))
    if k not in things_list:
        things_list.append((k, things_dict[k]))
        common_mass += things_dict[k]
    if common_mass > MAX_LOAD:
        things_list.pop()
        common_mass -= things_dict[k]
        break

variables_things_dict = dict(things_list)

print(variables_things_dict)



