"""
Задача 2:
Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
Ответьте на вопросы:
** какие вещи взяли все три друга
** какие вещи уникальны, есть только у одного друга
** какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей.
"""

things_dict = {
    'Андрей': ('топор', 'фонарь', 'палатка'),
    'Алексей': ('палатка', 'удочка', 'ружье'),
    'Сергей': ('палатка', 'ружье', 'топор')
}


all_things = set()
for items in things_dict.values():
    all_things |= set(items)

print("Все вещи, которые взяли друзья:")
print(all_things, end="\n\n")

list_user_things = [items for items in things_dict.values()]
uniq_for_each = {}

for k, v in things_dict.items():
    current_friend_things = set(v)
    temp_list = list_user_things.copy()
    temp_list.remove(v)
    for item in temp_list:
        current_friend_things -= set(item)

    if len(current_friend_things) == 0:
        uniq_for_each[k] = "Нет уникальных вещей"
    else:
        uniq_for_each[k] = current_friend_things

print("Примеры уникальных вещей для каждого из друзей:")
print(uniq_for_each, end="\n\n")


absent_things_each = {}

for k, v in things_dict.items():
    # current_friend_absent = all_things - set(v)
    # absent_things_each[k] = current_friend_absent
    current_friend_things = set(v)
    temp_list = list_user_things.copy()
    temp_list.remove(v)
    common_for_two = set()
    for item in temp_list:
        common_for_two |= set(item)

    absent_things_each[k] = common_for_two - current_friend_things

print("Примеры отсутствующих вещей для каждого из друзей:")
print(absent_things_each, end="\n\n")