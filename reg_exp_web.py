# Практическое задание к уроку 2. Регулярные выражения в работе с веб-страницей.
# 1. Получить количество учеников с сайта geekbrains.ru:
# a) при помощи регулярных выражений,
# b) при помощи библиотеки BeautifulSoup.
# Предварительно устанавливаем модуль requests. В cmd.exe вводим: > pip install requests ... В PyCrarm: File /
# Settings / Project Interpreter / «+» или нажать (Alt + Insert) / набрать имя модуля «requests» / нажать кн.
# «Install Package» / дожидаемся сообщ.  «Package ‘requests’ installed successfully» / закрываем окно / нажим. кн. «Ок»
from re import compile        # импортруем функцию compile для сбора рег. выражения в отдельный объект и исп. для поиска
from requests import get      # импортируем метод get из модуля requests
from bs4 import BeautifulSoup as b_s # импортируем BeautifulSoup из bs4. Предварит. устанавливаем аналочично requests
web_page = get('https://geekbrains.ru') # с помощью метода get() отправляем get запрос на страницу по адресу
page_text = web_page.text               # задаём в строке ниже рег. выражение для поиска
split_regex = compile("<span class=\"total-users\">[а-яА-Я\s]+([0-9\s]+)[а-яА-Я\s]+</span>")
number_of_students = split_regex.findall(page_text)  # находим количество человек
print('Количество учеников с сайта geekbrains.ru: ')
print(f'a) при помощи регулярных выражений:     %s' % ', '.join(number_of_students))
soup = b_s(page_text, "html.parser")
str_num_of_students = soup.find("span",{"class":"total-users"}).string   # строка 'Нас уже (какое то число) человек'
count_of_students = " ".join(filter(lambda s: s.isnumeric(),str_num_of_students.split())) # выбираем числа из строки
print(f'b) при помощи библиотеки BeautifulSoup: {count_of_students}')