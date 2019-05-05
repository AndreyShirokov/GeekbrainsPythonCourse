# 2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

# функция, принимающая на вход 3 числа и возвращающая наибольшее из них.
# Реализация без использования встроенных функций.
def max_of_3_numbers(number1, number2, number3):
    if number1 > number2:
        if number1 > number3:
             return number1
        else:
            return number3
    else:
        if number2 > number3:
            return number2
        else:
            return number3
# ----------------------------------------------------------------------------------------------------------------------
# функция, принимающая на вход 3 числа и возвращающая наибольшее из них.
# Реализация с использованием встроенной функции max
def max_of_3_numbers2(number1, number2, number3):
    return max(number1, number2, number3)
# ----------------------------------------------------------------------------------------------------------------------
# запрашиваем с клавиатуры три числа
number_1 = int(input('Введите 1-е число: '))
number_2 = int(input('Введите 2-е число: '))
number_3 = int(input('Введите 3-е число: '))
# вызов функций
print('Наибольшее из введённых чисел ', end='')
print(max_of_3_numbers(number_1, number_2, number_3), end='')
print('. Реализация без использования встроенных функций.')
print('Наибольшее из введённых чисел ', end='')
print(max_of_3_numbers2(number_1, number_2, number_3), end='')
print('. Реализация с использованием встроенной функции max.')