# 2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.
# Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
from random import choice


def random_element(some_list):
    if some_list:                   # если список пуст, то возвращает False. Иначе - True
        return choice(some_list)    # определяем случ. элемент
    else:
        return None                 # список пуст


if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    players_list = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
    empty_list = []
    print('Случайный элемент в списке {} это {}.'.format(my_list, random_element(my_list)))
    print('Случайный элемент в списке {} это {}.'.format(players_list, random_element(players_list)))
    print('Случайный элемент в списке {} это {}.'.format(empty_list, random_element(empty_list)))
