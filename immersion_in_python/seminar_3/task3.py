"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""
import string

usr_string = """
aa aaa aaa aaa a a a, a a aaa a aa fff 
fff fff fff ggg g g g g gggg g g g g 
ggggg g g g g g h h h h h h hh hhhh h h h 
asdasdasd asd, asd asd asd as ddas
""".translate(str.maketrans('', '', string.punctuation))

MAX_WORDS_PRINT = 10
STEP_COUNT = 1
NULL = 0
iteration = 1

words_list = [item for item in usr_string.split()]

counter_dict = dict()

for word in words_list:
    counter_dict[word] = counter_dict.get(word, NULL) + STEP_COUNT

sorted_counter_dict = dict(sorted(counter_dict.items(), key=lambda item: item[1], reverse=True))

for k, v in sorted_counter_dict.items():
    if iteration > MAX_WORDS_PRINT:
        break
    print(f"{iteration}) {k} - встречается {v} раз")
    iteration += 1
