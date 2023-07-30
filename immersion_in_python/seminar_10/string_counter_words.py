import string


class StringWords:
    MAX_WORDS_PRINT = 10
    STEP_COUNT = 1
    NULL = 0
    iteration = 1

    def __init__(self, user_string):
        self.usr_string = user_string.translate(str.maketrans('', '', string.punctuation))
        self.sorted_counter_dict = None

    def counter_words(self) -> dict[str, int]:
        """Функция подсчета слов в строке с записью в словарь"""
        words_list = [item for item in self.usr_string.split()]
        counter_dict = dict()

        for word in words_list:
            counter_dict[word] = counter_dict.get(word, self.NULL) + self.STEP_COUNT

        self.sorted_counter_dict = dict(sorted(counter_dict.items(), key=lambda item: item[1], reverse=True))

        return self.sorted_counter_dict


usr_string = """
aa aaa aaa aaa a a a, a a aaa a aa fff 
fff fff fff ggg g g g g gggg g g g g 
ggggg g g g g g h h h h h h hh hhhh h h h 
asdasdasd asd, asd asd asd as ddas
"""

counter = StringWords(usr_string)

print(counter.counter_words())
