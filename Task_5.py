# 5. Ссылки на страницы какого домена встречаются чаще всего?
from re import compile        # импортруем функцию compile для сбора рег. выражения в отдельный объект и исп. для поиска
from collections import Counter       # импортруем словарь, который позволяет считать количество вхождений слов в текст
with open('text.txt', 'r', encoding="utf-8") as text_file:          # открываем файл (в текущ. папке) на чтение
    text_from_file = text_file.read()                               # Читаем текст из файла.
print(text_from_file)                                               # выводим текст на экран.
print('-'*38) # выводим разделитель для удобства чтения
#split_regex = compile("\w*\.?\w+\.ru")             # поиск доменов. пример - travel.mail.ru (ответ: встречается 2 раза)
split_regex = compile("\w+\.ru")                    # поиск доменов. пример - mail.ru (ответ: встречается 3 раза)
domains = split_regex.findall(text_from_file)
lower_domains = [domain.lower() for domain in domains]  # переводим найденые домены в нижний регистр
print('Выводим все найденные в тексте домены: '         # для подсчёта количества вхождений
      '%s.' % ', '.join(lower_domains))         # выводим список доменов в нижнем регистре через запятую
counter_domains = Counter(lower_domains)        # подсчитываем количество вхождений каждого домена в тексте
max_val = max(counter_domains.values())         # подсчитываем максимальное количество вхождений доменов в текст
# создаём список доменов с максимальным количеством вхождений в текст
max_domains = [domain for domain, val in counter_domains.items() if val == max_val]
print(f'Ссылки на страницы этого(их) домена(ов) встречаются чаще всего - {max_val} раз(а): '
       '%s.' % ', '.join(max_domains))
