# 1. Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
# определяем функцию...
def habitat(name, age, city):
    return name + ', ' + age + ' год(а), проживает в городе ' +city # формируем возвращаемую строку
# запрашиваем с клавиатуры имя, возраст, город
name = input('Введите своё имя: ')
age = input('Введите возраст: ')
city = input('Введите город, где вы живёте: ')
# выводим данные в консоль
print(habitat(name, age, city))