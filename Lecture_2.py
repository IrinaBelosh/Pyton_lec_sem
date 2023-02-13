# # Урок 2. Данные, функции и модули в Python -
# # Знакомство с языком Python (лекции)

# # 1. Работа с файлами
# #     а) создать переменную и связать её с необходимым файлом
# #     б) указать путь к файлу
# #     в) определить модификатор работы
# #         a - добавление данных (можно несуществующий, тогда он создасться)
# #         r - чтение данных
# #         w - запись данных (можно несуществующий, тогда он создасться)
# #         w+, r+

# colours = ['red', 'blue', 'green']
# data = open('file.txt', 'a') # создаем переменную и связываем её с файломи указываем режим работы с ним
# data.writelines(colours) #Записываем в файл данные из списка
# data.write('\nline1\n')
# data.write('line2\n')
# data.close() # разрываем подключение переменнгой с файлом
# # создастся файл, в котор# ый при кажом запуске будут добавляться данные

# colours = ['red', 'blue', 'green3']
# data = open('file.txt', 'w')  # будут записываться только изменения
# data.writelines(colours)
# data.close()

# # Можно использовать конструкцию WITH
# with open('file.txt', 'w') as data:
#     data.write('line1\n')
#     data.write('line2\n')
# # При использовании этой конструкции, разрыв переменной с файлом происходит автоматически


# # Для чтения
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# # -----------------------------------------
# # Функции и модули
# # Функции можно дергать из других файлов

# import hello_script
# print(hello_script.f(5)) # Почему-то выдает еще и тип переменной

# # Можно присвоить алиас файлу
# import hello_script as x
# print(x.f(5))

# # Работа с аргументами функции
# # Для работы указываем нужное количество аргументов
# def new_string(symbol, count):
#     return symbol*count
# print(new_string('!', 5)) #!!!!!

# # Если один из аргументов задан по умолчанию, то можно пользоваться только одним
# def new_string(symbol, count=3):
#     return symbol*count
# print(new_string('!')) #!!!

# def new_string(symbol, count=3):
#     return symbol*count
# print(new_string(4)) # 12

# # При этом если указать второй элемент, он будет браться из указанного, а не по умолчанию
# def new_string(symbol, count=3):
#     return symbol*count
# print(new_string('!', 5)) # !!!!!

# # Есть возможность передачи неограниченного количества аргументов
# # Для этого при  её описании перед аргументом надо поставить звездочку
# def con(*param):
#     res: str = '' # Задаем тип данных аргументов
#     for item in param:
#         res += item
#     return res

# print(con('1','7','g','t','e')) # результат 17gte (строка)
# print(con(1,2,3,4,5)) # результат Error (несовпадение типа данных)

# # -----------------------------------------------------------
# # Рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# # ------------------------------------------------------------
# # Кортеж - неизменяемый список (tuple)
# t = ()
# print(type(t)) #<class 'tuple'>
# t = (1,) # Кортеж из одной координаты
# print(type(t)) #<class 'tuple'>
# t = (1) # not a tuple
# print(type(t)) # <class 'int'>
# t = (23, 67, 87)
# print(type(t)) # <class 'tuple'>
# colours = ['red', 'green', 'blue']
# print(colours) #['red', 'green', 'blue']
# print(type(colours)) # <class 'list'>
# t = tuple(colours) # Приведение к кортежу
# print(t) #('red', 'green', 'blue')
# print(type(t)) #<class 'tuple'>

# # Пример
# a = (3,4)
# print(a) #(3,4)

# # Обращаемся к элементам как со списком
# a = (3,4)
# print(a[0]) #3
# # Но не можем присваивать принудительно значения элементам
# # a[0] = 12 # Error
# for e in a:
#     print(e)

# # Распаковка кортежа
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r: {}, g: {}, b: {}'.format(red, green, blue))

# # -------------------------------------------------------------
# # Словари - неупорядоченные коллекции производльных объектов с доступом по ключу
# dictionary = {}  # Создаем пустой словарь
# dictionary = \
#     {
#         'left': '->',
#         'right': '<-',
#         'up': '#',
#         'down': '*'
#     }  # задаем элементы списка (\ позволяет не писать все элементы в одну строчку)
# print(dictionary)  # {'left': '->', 'right': '<-', 'up': '#', 'down': '*'}
# print(dictionary['left'])  # ->

# for k in dictionary.keys(): # Распечатываем все ключи
#     print(k)

# for k in dictionary.values(): # Распечатываем все значения
#     print(k)

# for v in dictionary: # Распечатываем всё (значения и ключи)
#     print(v)

# for v in dictionary: # Распечатываем все значения
#     print(dictionary[v])

# for item in dictionary: # Печатаем словарь парами (ключ\значение)
#     print('{}, {}'.format(item, dictionary[item]))

# # Присвоение нового значения по ключу
# dictionary['up'] = '^'
# print(dictionary)

# # ---------------------------------------------------------
# # Множества (set)
# colours = {'red', 'green', 'blue'} # Задаем множества
# print(colours)
# colours.add('gray') # Добавляем элемент в начало списка
# print(colours)
# colours.remove('red') # Просто удаляет имеющийся элемент, если его нет, то выдает ошибку
# print(colours)
# # colours.remove('red') # KeyError: 'red' (такого элемента уже нет)
# # print(colours)
# colours.discard('red') # Удаляет элемент, если его нет, то не выдает ошибку
# print(colours)
# colours.clear() # Очищаем множество
# print(colours) #set()

# a = {1, 2, 3, 4, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)
# print(f'\n{a}\n{b}\n{c}\n{u}\n{i}\n{dl}\n{dr}')

# # Можно делать такие миксы (\ - перенос)
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))

# s = frozenset(a) # Замороженное (неизменяемое) множество, изменяющие функции с ними работать не будут

# list1 = [1,2,3,4,5]
# print(list1.pop()) # Извлекает из списка последний элемент
# print(list1)

# list1 = [1,2,3,4,5]
# print(list1.pop(2)) # Извлекает из списка указанный элемент
# print(list1)

# list1 = [1,2,3,4,5]
# print(list1.insert(2,432)) # Вставляет элемент на нужную позицию (позиция, элемент)
# print(list1)

# list1 = [1,2,3,4,5]
# print(list1.append(32)) # Вставляет элемент в конец
# print(list1)

