# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# Получить объект — словарь из предыдущего задания.
import pickle
import json
if __name__ == '__main__':
    print('Чтение данных из файла group.pickle: ')
    with open('group.pickle', 'rb') as group_file:
        my_favourite_group = pickle.load(group_file)
    print(my_favourite_group)
    print('Чтение данных из файла group.json: ')
    with open('group.json', 'r', encoding='utf-8') as group_file_json:
        my_favourite_group_json = json.load(group_file_json)
    print(my_favourite_group_json)