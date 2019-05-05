# Урок 6. ООП (продолжение)
# 1. Создайте классы Noun и Verb.
# 2. Настройте наследование от Word.
# 3. Добавьте защищенное свойство «Грамматические характеристики».
# 4. Перестройте работу метода show класса Sentence, чтобы метод строил предложение.
# 5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.


class Word:     # Создаём класс Word (слово) со свойствами text и part of speech (часть речи).
    def __init__(self, init_text = '', init_part_of_speech = ''):  # Добавляем возможность создавать объект слово
        self.text = init_text                                      # со значениями в скобках. Устанавливаем начальн.
        self.part_of_speech = init_part_of_speech                  # значения свойств через аргументы конструктора


class Noun(Word):  # Создаём класс Noun (Сущ.). Родительский класс Word помещаем в скобки после Noun.            (1 и 2)
    def __init__(self,init_text = '', init_gram_charact = []):
        super().__init__(init_text, 'существительное')  # Вызываем конструктор родительского класса
        self._gram_charact = init_gram_charact  #Добавл. защищ. (с 1-м подчёрк.) свойство «Грамматич. характерист.». (3)
    def get_gram_charact(self):                 # добавляем метод получения защ. свойства
        return self._gram_charact

class Verb(Word):  # Создаём класс Verb (глаг.). Родительский класс Word помещаем в скобки после Noun.           (1 и 2)
    def __init__(self,init_text = '', init_gram_charact = []):
        super().__init__(init_text, 'глагол')           # Вызываем конструктор родительского класса
        self._gram_charact = init_gram_charact  #Добавл. защищ. (с 1-м подчёрк.) свойство «Грамматич. характерист.». (3)
    def get_gram_charact(self):                 # добавляем метод получения защ. свойства
        return self._gram_charact

class Sentence:  # Создаём класс Sentence (предлож.) со свойств. content - список ном. слов, list_of_words - список слов
    def __init__(self, init_num_words_list = [], init_words_list = []):  # Определяем конструктор класса Sentence
        self.content = init_num_words_list                     # Устанавливаем начальные значения
        self.list_of_words = init_words_list                   # свойств через аргументы конструктора

    def show(self):  # метод show по-прежнему корректно составляет предложение. Изменения не потребовались           (4)
        result = [self.list_of_words[i-1].text for i in self.content]   # формируем список слов в правильном порядке.
        str_result = ' '.join(result)                      # соединяем слова через пробел.
        str_result = str_result.capitalize()               # 1-й символ строки переводим в верхний регистр
        return f'{str_result}.'                            # возвращаем строку (предложение), в конце ставим точку.

    def print_sentence(self):                              # метод, выводящий в консоль предложение.
        print(self.show())

    def show_parts(self):                         # метод show_parts показывает грамматич. характерист. сущ. и глаг. (5)
        result = []
        for one_word in self.list_of_words:
            if one_word.__class__.__name__ != 'Word':       # если это экз. класса Noun или Verb, то
                result.append(one_word.get_gram_charact())  # добавляем в список грамматические характеристики
        return result                                       # возвращаем список грамматических характеристик

    def print_show_parts(self):                            # метод, выводящий в консоль список грамматич. характеристик.
        print(self.show_parts())


if __name__ == '__main__': # в стр. ниже создаём объект obj_sentence - экз. класса Sentence
    obj_sentence = Sentence([5, 1, 3, 4, 2], [Noun('программу', ['неодуш.', 'ед. число.']),
                                              Word('завтра', 'наречие'),
                                              Noun('телепередач', ['неодуш.', 'ед. число.']),
                                              Word('на', 'предлог'),
                                              Verb('посмотрите', ['несоверш.', 'буд. врем.'])])
# В стр. выше также устанавливаем начальн. значения свойств объекта через аргументы конструктора класса Sentence:
# 1. content - задаём порядок слов, входящих в предложение - [5, 1, 3, 4, 2]
# 2. list_of_words - создаём 5 объектов - экз. классов Word, Noun, Verb формируем из них список слов, входящих в предлож.
# Устанавливаем начальн. значения свойств всех объектов через аргументы конструкторов классов Word, Noun, Verb.
    obj_sentence.print_sentence()       # Выводим в консоль предложение для тестирования работы метода show.
    obj_sentence.print_show_parts()     # Выводим в консоль грамматические характерист. для тестир. работы  show_parts.