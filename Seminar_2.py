# Задача 1. Напишите программу, которая на вход принимает число N
# и выдает последовательность из N членов.
# Пример:
# in >> 5
# out >> 1, -3, 9, -27, 81

# Вариант 1

n = int(input('Enter a number: '))

for i in range(n):
    print((-3)**i, end = ', ')

# Вариант 2
n = int(input('Enter a number: '))
seq = 1

for i in range(n):
    print(seq, end=', ')
    seq*=-3

# Задача 2. Создайте список длины n, значения формируются по формуле
# 3k+1 где k принимает значение от 1 до n
# Пример
# n >> 3
# out >> [4, 7, 10]

import os # последовательность чистит консоль
clear=lambda:os.system('cls')
clear()

n = int(input('Enter a number: '))
num_list = []

for k in range(1, n+1):
    num_list.append(3*k+1)
print(num_list)

# Задача 3. Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять количество
# вхождений одной строки в другой
# Например
# in >> gipopotampo
#    >> po
# out >> 3

import os  # последовательность чистит консоль
def clear(): return os.system('cls')

clear()

n = input('Enter the line: ')
m = input('What are you looking for? ')

print(n.count(m))

