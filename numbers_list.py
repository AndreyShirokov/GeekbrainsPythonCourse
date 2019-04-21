# 2. Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
#       1. Элемент кратен 3,
#       2. Элемент положительный,
#       3. Элемент не кратен 4.
#           Примечание: Список с целыми числами создайте вручную в начале файла.
#           Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
#----------------------------------------------------------------------------------------------------------------------
# Примечание: также можно создать список из 20-ти случайых целых чисел N, (-100 ≤ N ≤ 100). Следующие 2 строки.
# from random import randint
# list_of_numbers = [randint(-100, 100) for i in range(20)]
list_of_numbers = [-83, -72, 31, 76, 27, -72, 92, 86, -18, 68, 44, 57, -50, 4, -45, -60, 77, -32, -31, 28]
list_divisible_of_three = [number for number in list_of_numbers if number % 3 == 0]
list_of_positive = [number for number in list_of_numbers if number > 0]
list_not_divisible_of_four = [number for number in list_of_numbers if number % 4 != 0]
print(f'Исходный список чисел     : {list_of_numbers}')
print(f'Cписок чисел, кратных 3   : {list_divisible_of_three}')
print(f'Cписок положительных чисел: { list_of_positive}')
print(f'Cписок чисел, не кратных 4: { list_not_divisible_of_four}')