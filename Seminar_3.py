# Задача 1. Задайте список из произвольных чисел, количество задает пользователь.
# Напишите программу определяющую присутствует ли в заданном списке
# число, полученное от пользователя.
# Пример
# in  10
#     2
# out [13,45,2,7,65,2]
#     'The number 2 is present in the list'

import os
clear = lambda:os.system('cls')
clear()

# # Первый способ
# import random # Вызываем модуль
# import.sample() # Обращаемся к функции модуля


from random import sample # Второй способ вызова

def find_number (f_length, f_number):
    my_list = sample(range((f_length+1)*2), f_length)
    print(my_list)
    if f_number in my_list:
        return 'YES'
    return 'NO'

# answer = find_number(length, number)
# print(answer)

# Вариант без отдельного воода данных от пользователя (всё в одну строку)
answer = find_number(int(input('Enter the number of elements: ')),\
    int(input('Enter the element to look for: ')))
print(answer)

# --------------------------------------------
# Задача 2. Задайте список из произвольных слов, количество задает пользователь
# Напишите программу, которая определит индекс второго вхождения строки
# в списке, либо сообщит, что её нет.
# Например:
# in -> 4
#     -> 'xyz'
# out -> ['xyz', 'zyx', 'yzx', 'xyz']
#     -> 4

from random import sample


def form_list(number, word='abc'):
    f_list = []
    for i in range(number):
        element = sample(word, k=3)
        f_list.append(''.join(element))
    return f_list


def find_second_word(in_list, word):
    if word in in_list and in_list.count(word) > 1:
        first_index = in_list.index(word)
        print(in_list.index(word, first_index+1))
    else:
        print('No second index')

my_list = form_list(int(input('Enter the number of elements: ')))
print(my_list)
find_second_word(my_list, input('Enter a word to look for: '))
