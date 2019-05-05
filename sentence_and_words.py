# 1. Создайте класс Word.
# 2. Добавьте свойства text и part of speech.
# 3. Добавьте возможность создавать объект слово со значениями в скобках.
# 4. Создайте класс Sentence
# 5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
# 6. Добавьте метод show, составляющий предложение.
# 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.


class Word:                                               # Создаём класс Word (слово).                              (1)
    text = 'unknown'                                      # Добавляем свойство text.                                 (2)
    part_of_speech = 'unknown'                            # Добавляем свойство part of speech (часть речи).          (2)

    def __init__(self, init_text, init_part_of_speech):   # Добавляем возможность создавать объект слово             (3)
        self.text = init_text                             # со значениями в скобках. Устанавливаем начальн.
        self.part_of_speech = init_part_of_speech         # значения свойств через аргументы конструктора


class Sentence:                                           # Создаём класс Sentence (предложение)                     (4)
    content = []                                          # Добавляем список номеров слов, входящих в предложение.   (5)
    list_of_words = []                                    # Добавляем список слов, входящих в предложение.

    def __init__(self, init_num_words_list, init_words_list):  # Определяем конструктор класса Sentence
        self.content = init_num_words_list                     # Устанавливаем начальные значения
        self.list_of_words = init_words_list                   # свойств через аргументы конструктора

    def show(self):                                        # метод show, составляющий предложение.                   (6)
        result = [self.list_of_words[i-1].text for i in self.content]   # формируем список слов в правильном порядке.
        str_result = '%s.' % ' '.join(result)              # соединяем слова через пробел, в конце ставим точку
        str_result = str_result.capitalize()               # 1-й символ строки переводим в верхний регистр
        return str_result                                  # возвращаем строку (предложение).

    def print_sentence(self):                              # метод, выводящий в консоль предложение.
        print(self.show())

    def show_parts(self):                                  # метод, отображающий, какие части речи входят в предлож. (7)
        result = [self.list_of_words[i-1].part_of_speech for i in self.content]  # формируем список частей речи
        result = set(result)                               # исколючаем повторения, без этой строки выводит с повторен.
        str_result = 'Части речи, входящие в предложение: %s.' % ', '.join(result)  # соединяем ч.р. через "," в конце "."
        return str_result                                  # возвращаем строку

    def print_show_parts(self):                            # метод, выводящий в консоль части речи, входящие в предложен.
        print(self.show_parts())


if __name__ == '__main__': # в стр. ниже создаём объект obj_sentence - экз. класса Sentence
    obj_sentence = Sentence([5, 1, 3, 4, 2], [Word('программу', 'существительное'), Word('завтра', 'наречие'),
                                              Word('телепередач', 'существительное'), Word('на', 'предлог'),
                                              Word('посмотрите', 'глагол')])
    # В стр. выше также устанавливаем начальн. значения свойств объекта через аргументы конструктора класса Sentence:
    # 1. content - задаём порядок слов, входящих в предложение - [5, 1, 3, 4, 2]
    # 2. list_of_words - создаём 5 объектов - экз. класса Word, формируем из них список слов, входящих в предложение.
    # Устанавливаем начальн. значения свойств всех объектов через аргументы конструктора класса Word.
    obj_sentence.print_sentence()       # Выводим в консоль предложение для тестирования работы метода show.
    obj_sentence.print_show_parts()     # Выводим в консоль части речи для тестирования работы метода show_parts.