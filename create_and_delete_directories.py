# 1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py). В нем напишите функцию, создающую
# директории от dir_1 до dir_9 в папке, из которой запущен данный код. Затем создайте вторую функцию,
# удаляющую эти папки. Проверьте работу функций в этом же модуле.
from os import getcwd, mkdir, rmdir, path, listdir


def make_nine_dir():
    current_directory = getcwd()                                                 # получаем текущую директорию
    for directory_number in range(1,10):                                         # цикл от 1 до 9
        new_path = path.join(current_directory, f"dir_{directory_number}")       # определяем новые пути
        mkdir(new_path)                                                          # создаём каталоги


def del_nine_dir():
    current_directory = getcwd()                                                 # получаем текущую директорию
    for directory_number in range(1, 10):                                        # цикл от 1 до 9
        new_path = path.join(current_directory, f"dir_{directory_number}")       # определяем новый путь
        rmdir(new_path)                                                          # создаём каталог


def check_nine_dir():                                               # Проверяем папки, содержащие в имени "dir_"
    print_string = 'Папок, содержащих в имени "dir_" не найдено.'
    dirs = listdir(getcwd())                                        # получаем текущую директорию
    for file in dirs:
        if file.find('dir_') != -1:                                 # если есть папка, содержащая "dir_"
            print_string = 'Найдены папки, содержащие в имени "dir_". Все они перечислены ниже:'
            break
    print(print_string)
    for file in dirs:
        if file.find('dir_') != -1:
            print(' {}'.format(file), end='')                        # выводим все такие папки "dir_?"
    print('')

if __name__ == '__main__':
    print('Создаём директории от dir_1 до dir_9 в папке, из которой запущен данный код.')
    make_nine_dir()
    print('Проверяем директории от dir_1 до dir_9 в папке, из которой запущен данный код.')
    check_nine_dir()
    print('Удаляем директории от dir_1 до dir_9 в папке, из которой запущен данный код.')
    del_nine_dir()
    print('Проверяем директории от dir_1 до dir_9 в папке, из которой запущен данный код.')
    check_nine_dir()

