# 1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
import pickle
import json
my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016}, {'name': 'Шапито','year': 2014}]}
if __name__ == '__main__':
    print('Cериализуем данный словарь с помощью pickle в байты, выводим результаты в терминал:')
    print(pickle.dumps(my_favourite_group))
    print('Cериализуем данный словарь  с помощью json в json, выводим результаты в терминал:')
    print(json.dumps(my_favourite_group))
    # Записываем результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
    with open('group.pickle', 'wb') as group_file:
        pickle.dump(my_favourite_group, group_file)
    print('Cловарь для любимой музыкальной группы записан в файл group.pickle.')
    with open('group.json', 'w', encoding='utf-8') as group_file_json:
        json.dump(my_favourite_group, group_file_json)
    print('Cловарь для любимой музыкальной группы записан в файл group.json.')
