# 3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.
from random_list_element import random_element
# Попробовал строку ниже. Ошибок нет, но так не рекомендуется в видеоуроках
# from create_and_delete_directories import *
# Но лучше так, как в следующей строке
from create_and_delete_directories import make_nine_dir, del_nine_dir, check_nine_dir
# проверяем работу ф-ций из додуля create_and_delete_directories
print('Создаём директории от dir_1 до dir_9 в папке, из которой запущен данный код.')
make_nine_dir()
print('Проверяем директории от dir_1 до dir_9 в папке, из которой запущен данный код.')
check_nine_dir()
print('Удаляем директории от dir_1 до dir_9 в папке, из которой запущен данный код.')
del_nine_dir()
print('Проверяем директории от dir_1 до dir_9 в папке, из которой запущен данный код.')
check_nine_dir()
# проверяем работу ф-ций из додуля random_list_element
my_list = [1, 2, 3, 4]
players_list = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
empty_list = []
print('случайный элемент в списке {} это {}'.format(my_list, random_element(my_list)))
print('случайный элемент в списке {} это {}'.format(players_list, random_element(players_list)))
print('случайный элемент в списке {} это {}'.format(empty_list, random_element(empty_list)))