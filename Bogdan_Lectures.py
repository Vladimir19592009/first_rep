

# my_set = {5, 4, 8, 9, 1}
# print(my_set)
# my_set.add(38)
# print(my_set)

# my_other_set = {9, 4, 1, 35, 10}
# print(my_other_set)

# new_set = (my_set.intersection(my_other_set))
# print(new_set)
# new_set = list(new_set)
# print(new_set)

# my_range = range(5)

# print(dir(my_range))

# print(my_range)
# print(type(my_range))
# print(my_range[-1])

# for n in my_range:
#     print(n, end=" ")


# ВСТРОЕННАЯ ФУНКЦИЯ zip:

# fruits = ['apple', 'banana', 'lime']
# nums = [100, 70, 50]
# fruit_num_zip = zip(fruits, nums)
# print(fruit_num_zip)
# # <zip object at 0x000001B6FD781B40>
# # полученный объект легко можно конвертировать в список кортежей и т.о произвеси слияние 2-х списков:
# можно и трёх списков (кортежи будут состоять из 3-х элементов)

# fruit_num_list = list(fruit_num_zip)
# print(fruit_num_list)
# # [('apple', 100), ('banana', 70), ('lime', 50)]

# Большее количество  элементов в одном из списков игнорируется Python.


# КОНВЕРТАЦИЯ ZIP В DICT: (только из 2-х сисков)

# fruits = ['apple', 'banana', 'lime'] # первая последовательность для ключей
# nums = [100, 70, 50]                 # вторая последовательность для значений
# fruit_num_zip = zip(fruits, nums)
# print(fruit_num_zip)
# # <zip object at 0x000001B6FD781B40>

# fruit_num_dict = dict(fruit_num_zip)  # или одной строкой: fruit_num_dict = dict(zip(fruits, nums))
# print(fruit_num_dict)
# # {'apple': 100, 'banana': 70, 'lime': 50}
# -------------------------------------------------------------

# def increase_person_age(person):
#     person_copy = person.copy()
#     person_copy['age'] += 1
#     return person_copy

# person_one = {'name': 'Bob', 'age': 21}
# print(id(person_one))

# new_person = increase_person_age(person_one)
# print(new_person['age'])  # 22
# print(person_one['age'])  # 21
# --------------------------------------------------------------

# Написать ф-ию, которая объединяет два списка в словарь посредством ф-ии zip

# def merge_list_to_dict(a_lst, b_lst):
#     return dict(zip(a_lst, b_lst))

# a_lst = ['Bob', 'Alice', 'Tom', 'Jack']
# b_lst = [25, 23, 22, 24]

# my_dict = merge_list_to_dict(a_lst, b_lst)
# print(my_dict)
# # {'Bob': 25, 'Alice': 23, 'Tom': 22, 'Jack': 24}


# def sum_num(*args):
#     # посмотрим что это такое?:
#     print(args)         # (2, 3, 7)
#     print(type(args))   # <class 'tuple'>
#     print(args[0])      # 2
#     return sum(args)    # 12

# print(sum_num(2, 3, 7))


# ПОЗИЦИОННЫЕ АРГУМЕНТЫ:

# def get_posts_info(name, posts_qty):
#     info = f'{name} wrote {posts_qty} posts'
#     return info

# info = get_posts_info('Vladimir', 25)
# print(info)
# # Vladimir wrote 25 posts


# АРГУМЕНТЫ С КЛЮЧЕВЫМИ СЛОВАМИ:

# def get_posts_info(name, posts_qty):
#     info = f'{name} wrote {posts_qty} posts'
#     return info

# info = get_posts_info(name='Vladimir', posts_qty=25)  # Порядок аргументов не важен (присутствуют ключевые слова)
# print(info)
# # Vladimir wrote 25 posts


# ОБЪЕДИНЕНИЕ АРГУМЕНТОВ В СЛОВАРЬ:

# ---------------------------------------------------------------------------
# def get_posts_info(**person):
#     print(person)
#     info = (f'{person['name']} wrote'
#             f'{person['posts_qty']} posts')
#     return info

# info = get_posts_info(name='Vladimir', posts_qty=25)
# print(info)
# # Vladimir wrote25 posts
# ----------------------------------------------------------------------------

# def update_car_info(**car):
#     car['is_available'] = True
#     return car

# print(update_car_info(brand='BMV', price=100000))
# # {'brand': 'BMV', 'price': 100000, 'is_available': True}
# ----------------------------------------------------------------------------

# ЗНАЧЕНИЯ ПАРАМЕТРОВ Ф-ИИ ПО УМОЛЧАНИЮ (пример)

# from datetime import date


# def get_weekday():     # возвращает день недели (например: вториник)
#     return date.today().strftime('%A')


# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()   # копию создаём для сохранения внешних аргументов(initial_post) в неприкосновенности

#     # ниже сздаём и вставляем в словарь новую пару (ключ: значение)
#     post_copy['created_on weekday'] = weekday
#     return post_copy


# initial_post = {'id': 243,
#                 'author': 'Vladimir',
#                 }

# post_with_weekday = create_new_post(initial_post)
# print(post_with_weekday)
# # {'id': 243, 'author': 'Vladimir', 'created_on weekday': 'Thursday'}
# print(initial_post)


# КОЛБЭК ФУНКЦИИ  (передается как аргумент в другую ф-цию и там вызывается)

# def print_number_info(num):
#     if num % 2 == 0:
#         print("Entered nuber is even")
#     else:
#         print("Entered nuber is odd")


# def process_nuber(num, callback_fn):
#     callback_fn(num)


# entered_num = int(input("Enter any number: "))  # Enter any number: 46
# process_nuber(entered_num, print_number_info)
# # Entered nuber is even

# В вызывающей ф-ии process_nuber в качестве второго аргумента можем применить другой аргумент который будет использован другой ф-ией. Например:

# def print_number_info(num):
#     if num % 2 == 0:
#         print("Entered nuber is even")
#     else:
#         print("Entered nuber is odd")


# def print_square_num(num):
#     print('Square of the num is', num * num)


# def process_nuber(num, callback_fn):
#     callback_fn(num)


# entered_num = int(input("Enter any number: "))  # Enter any number: 46
# process_nuber(entered_num, print_number_info)
# # Entered nuber is even
# # применим другой аргумент (для print_square_num)
# process_nuber(entered_num, print_square_num)
# # Square of the num is 2116


# ПРАВИЛА РАБОТЫ С Ф-ЯМИ:

# 1. Называть ф-ии исходя из выполняемых задач
# 2. Названия ф-ий начинать с глагола
# 3. Одна ф-ия должна выполнять одну задачу
# 4. Не рекомендуется изменять внешние переменные

# Задача:
# 1. Создайте две переменные и присвойте им две одинаковые последовательности типа set (без копирования)
# 2. Выведите в терминал результат сравнения этих объектов, объясните результат
# 3. Используя оператор is сравните их, объясните результат
# 4. Проверте есть ли определенные элементы в множестве, используя оператор in

# my_set1 = {9, 15, 8, 3, 1, 4}
# my_set2 = {1, 8, 4, 15, 9, 3}
# print(id(my_set1))  # 2630168068832
# print(id(my_set2))  # 2630168354080
# print(my_set1 == my_set2)  # порядок элементов не имеет значения поэтому: True
# # оператор is сравнивает объекты в памяти ( id этих объектов разные) резудьтат: False
# print(my_set1 is my_set2)
# # Два варианта проверки наличия элементов в множестве
# print(15 in my_set1)
# print(20 in my_set2)

# if 1 not in my_set2:
#     print('True')
# else:
#     print('False')
# # False


# ЛОЖНЫЕ ЗНАЧЕНИЯ при приведении к логическому типу дают False:

# int = 0
# float = 0.0
# complex = 0j

# Проверим...
# print(bool(0))      # False
# print(bool(0.0))    # False
# print(bool(0j))     # False
# print(bool(None))   # False

# # а также пустой словарь {}, пустой список [], пустой кортеж (), пустая строка "" range(0), пустое множесто set()
# print(bool({}))         # False
# print(bool([]))         # False
# print(bool(()))         # False
# print(bool(""))         # False
# print(bool(range(0)))   # False
# print(bool(set()))      # False


# ЛОГИЧЕСКИЕ ОПЕРАТОРЫ:   not and  or

# Оператор <not>(НЕ) всегда возвращает значение типа <bool>, и используется в условных инструкциях <if>
# Операторы <and>(И) и <or>(ИЛИ) являются операторами <КОРОТКОГО ЗАМЫКАНИЯ> возвращают значение одного из операндов выражения, где они применялись.

# my_list = []
# print(not my_list)      # True
# print(not not my_list)  # False


# my_list = [1, 2]
# print(not my_list)      # False
# print(not not my_list)  # True

# my_list = [1, 2]
# other_list = ['a', 'b']
# print(my_list or other_list)  # [1, 2]

# my_list = [1, 2]
# other_list = []
# print(not my_list and not other_list)  # False
# -----------------------------------------------------------------------------

# my_dict1 = {'Tom': 25, 'Alice': 21, 'Peter': 32}
# my_dict2 = {'Alice': 21, 'Peter': 32, 'Tom': 25}

# if my_dict1 == my_dict2:
#     print('Словари идентичны')
# else:
#     print('Словари разные')

# print(my_dict2 and my_dict1)
# -----------------------------------------------------------------------------


# ОПЕРАТОР РАСПАКОВКИ СЛОВАРЯ (**)

# позволяет на основе родительского словаря создавать новый расширенный словарь:

# button = {'width': 200,
#           'text': 'Buy'}
# red_button = {**button,
#               'color': 'red'}
# print(red_button)   # {'width': 200, 'text': 'Buy', 'color': 'red'}
# print(button)       # {'width': 200, 'text': 'Buy'}   объект <button>  остается не мутированным
# ---------------------------------------------------------------------------------------

# grey_button = {'width': 200,
#           'text': 'Buy',
#           'color': 'grey'}

# red_button = {'color': 'red',
#               **grey_button}
# print(red_button)       # {'color': 'grey', 'width': 200, 'text': 'Buy'}
# print(grey_button)      # {'width': 200, 'text': 'Buy', 'color': 'grey'}
# ---------------------------------------------------------------------------------------

# grey_button = {'width': 200,
#           'text': 'Buy',
#           'color': 'grey'}

# red_button = {**grey_button,
#               'color': 'red'}
# print(red_button)       # {'width': 200, 'text': 'Buy', 'color': 'red'}
# print(grey_button)      # {'width': 200, 'text': 'Buy', 'color': 'grey'}


# ОБЪЕДИНЕНИЕ СЛОВАРЕЙ

# 1. с помощью <**>

# button_info = {'text': 'Buy'}

# button_style = {'color': 'yellow',
#                 'width': 200,
#                 'heirht': 300}

# button = {**button_info,
#           **button_style}

# print(button)
# # {'text': 'Buy', 'color': 'yellow', 'width': 200, 'heirht': 300}


# 2. с помощью оператора <|>;
# необходимо иметь в виду ключи второго словаря имеют приоритет, поэтому в случае одноимённых ключей в объединяемых словарях в итоговом словаре будут пары (ключ: значение) второго словаря. Оригинальные словари остаются не тронутыми.

# button_info = {'text': 'Buy'}

# button_style = {'color': 'yellow',
#                 'width': 200,
#                 'heirht': 300}

# button = button_info | button_style

# print(button)
# # {'text': 'Buy', 'color': 'yellow', 'width': 200, 'heirht': 300}


# ИНСТРУКЦИЯ DEL

# my_dict = {'a': True, 'b': 10}
# del my_dict['a']
# # аналогичная запись удаления элемента с помощью магического метода
# my_dict.__delitem__('b')
# print(my_dict)              # {}

# точно также инструкция del работает со строками.


# ФОРМАТИРОВАНИЕ СТРОК С f-string

# hello = 'Hello'
# world = 'world'

# greeting = f"{hello} {world}"
# print(greeting)                 # Hello world

# Пример: Сформировать и вывести строку info двумя способами в том числе используя f строку.

# my_name = 'Vladimir'
# my_hobby = 'running'
# time = 8

# # info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + " o'clock "
# info = f"{my_name} likes {my_hobby} at {time} o'clock"

# print(info)
# # Vladimir likes running at 8 o'clock

# info = info.title()     # Vladimir Likes Running At 8 O'Clock
# print(info)


# ЛЯМБДА Ф-ИИ  -  всегда анонимные. Выглядит так:

# lambda parameters: expression
# lambda параметры: выражение
# lambda a, b: a * b

# Пример:

# def greeting(greet):
#     return lambda name: f"{greet}, {name}!"


# mornig_greeting = greeting("Good Morning")
# print(mornig_greeting('Vladimir'))          # Good Morning, Vladimir!

# evening_greeting = greeting("Good Evening")
# print(evening_greeting('Vladimir'))         # Good Evening, Vladimir!


# ЗАДАЧА УСЛОВНЫЕ ИНСТРУКЦИИ

# 1. Создайте инструкцию <route_info>, которой будет передаваться словарь
# 2. Если в словаре есть ключ <distance> и его значение - целое число, верните строку <Distance to your distination is <distance>.
# 3. Иначе, если есть ключи <speed> and <time>, верните строку <Distance to your distination is speed * time>
# 4. Иначе верните строку <No distance info is available>.

# def get_inf(route):
#     if ('distsnce' in route) and (type(route['distance']) == int):
#         return f"Distance to your distination is {route['distance']}"
#     if ('speed' in route) and ('time' in route):
#         return f"Distance to your distination is {route['speed'] * route['time']}"
#     return "No distance info is available"


# print(get_inf({'distance': 100}))
# # No distance info is available
# print(get_inf({'speed': 10, 'time': 5}))
# # Distance to your distination is 50
# print(get_inf({'speed': 10}))
# # No distance info is available


# ТЕРНАРНЫЙ ОПЕРАТОР (условное выражение)

# Переменная(опционально) = Выражение_1 if Условие else Выражение_2

# При выполнении условия if выполняется Выражение_1 если условие ложное выполняется Выражение_2. Результат может быть присвоен Переменной.
# Тернарный оператор также применяется для вызова либо одной ф-ии либо другой в зависимости от выполнения условия if. Тогда вместо Выражения_1 и Выражения_2 будут стоять вызовы различных ф-ий.

# Пример 1

# my_number = 21.5

# print("is int") if type(my_number) is int else print("is not int")
# # is not int

# Пример 2
# здесь есть два вызова ф-ий (отправить изображение) и (обработать и отправить изображение).

# send_img(img) if img_get['is_processed'] else process_send_img(img)

# суть этого тернарного оператора: если в словаре img есть ключ <is_processed> (означает, что изображение уже обработано и его неоюходимо только отправить) вызывается ф-ия <send_img>. Если же ключ отсутствует, то вызывается другая ф-ия (обработать и отправить).

# Пример 3

# product_qty = 10    # кол-во продукции для продажи

# print("in stock" if product_qty > 0 else "out of stock")
# # in stock

# Задача:
# с помощью терн. оператора проверить длину строки (если длина строки больше 79 символов то вывести  сообщение "Длина строки большая", если меньше "Строка короткая")

# my_str = "c помощью терн. оператора проверить длину строки (если длина строки больше 79 символов то вывести  сообщение 'Длина строки большая', если меньше 'Строка короткая')"

# print("Длина строки большая" if len(my_str) > 79 else "Строка короткая")
# # Длина строки большая


# ЦИКЛЫ: используются для перебора элементов последовательностей (dict, list, tuple, set, range, str)

# применяются два типа циклов (for ... in ...) and ( while)

# for Элемент in Последовательность:
# Тело цикла

# my_list = [True, 10, 'abc', {}]     # для списков

# for elem in my_list:
#     print(elem, end=' ')
# # True 10 abc {}
# ------------------------------------

# video_info = ('1920x1080',True, 27)     # для котежей

# for elem in video_info:
#     print(elem, end=' ')
# # 1920x1080 True 27
# -------------------------------------

# my_object = {       # для словарей
#     'x': 10,
#     'y': True,
#     'z': 'abc'
# }

# for key in my_object:
#     print(key, my_object[key])
# # x 10
# # y True
# # z abc
# --------------------------------------

# Задача 1
# 1. Создайте ф-ию dict_to_list, которая будет конвертировать словарь в список еортежей.
# 2. Ф-ия должна принимать словарь, а возвращать список кортежей, в каждом кортеже должны быть пары (key, value) из словаря.
# 3. Если значение ключа - целое число, то его нужно умножить на 2 перед добавлением в кортеж.

# def dict_to_list(object):
#     list_conv = []
#     for k, v in object.items():
#         if type(v) is int:
#             v = v * 2
#         list_conv.append((k, v))
#     return list_conv


# print(dict_to_list({'x': 10, 'y': True, 'z': 'abc'}))
# [('x', 20), ('y', True), ('z', 'abc')]
# ---------------------------------------

# Задача 2
# 1. Создайте ф-ию filter_list, которая будет фильтровать список.
# 2. У ф-ии должно быть два параметра - список и тип значения.
# 3. Ф-ия должна вернуть новый список, в котором останутся только значения того типа, который был передан в вызове ф-ии вторым аргументом.
# 4. Ф-ию можно будет вызывать например так: filter_list([35, True, 'abc', 10], int) и получить [35, 10]


# def filter_list(your_list, your_type):
#     my_list = []
#     for val in your_list:
#         if type(val) is your_type:
#             my_list.append(val)
#     return my_list


# print(filter_list([35, True, 'abc', 10], int))
# # [35, 10]
# print(filter_list([35, True, 'abc', 10], str))
# # ['abc']
# print(filter_list([35, True, 'abc', 10], bool))
# # [True]

# ещё одно решение задачи с помощью лямбда ф-ии и метода фильтр:

# def filter_list(your_list, your_type):
#     return list(filter(lambda val: type(val) is your_type,
#                        your_list))


# print(filter_list([35, True, 'abc', 10], int))
# # [35, 10]
# print(filter_list([35, True, 'abc', 10], str))
# # ['abc']
# print(filter_list([35, True, 'abc', 10], bool))
# # [True]


# ЦИКЛ WHILE:
# Переход к следующей итерации с помощью CONTINUE:

# import random

# random_num = random.randint(1, 5)
# while True:
#     num = int(input("Guess the number from 1 to 5: "))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congratulation!", random_num)
#     break

# Задача:
# 1. Создайте цикл, в котором попросите пользователя ввести два числа в терминале.
# 2. Выведите в терминал результат деления первого числа на второе.
# 3. После спросите пользователя хочетли он продолжить (yes/no)
# 4. Если ноу, то нужно выйти из цикла
# 5. Иначе всё повторить сначала

# while True:
#     num_1 = float(input("Enter number one: "))
#     num_2 = float(input("Enter number two: "))

#     print(num_1/num_2)
#     answer = input("Do you want to continue (yes/no)?: ")
#     if answer == "no":
#         break


# То же самое но с обработкой ошибки ввода чисел (ValueError):

# while True:
#     try:
#         num_1 = float(input("Enter number one: "))
#         num_2 = float(input("Enter number two: "))
#     except ValueError as e:
#         print(e)
#         print("You must enter numbers!")
#         continue
#     print(num_1/num_2)
#     answer = input("Do you want to continue (y = yes)?: ")
#     if answer == "y":
#         continue
#     else:
#         break


# СОКРАЩЁННЫЙ ЦИКЛ <FOR IN>:
# - используется для создания новых последовательностей на основании существующей:
# - может применяться для list(список), dictionary(словарь), tuple(кортеж), set(множество).

# имеет общий вид:     Выражение for Элемент in Последовательность if Условие

# В этом цикле Вырвжение и Условие имеют доступ к Элементу. Т.е. Условием мы можем отфильтровать элементы Последовательности. Кроме того Элементы новой последовательности могут быть изменены посредством Выражения.

# Пример 1:
# -сформируем новый список (абсолютных значений) в обычном for in:

# all_nums = [-3, 1, 0, 10, -20, 5]
# absolute_num = []

# for num in all_nums:
#     absolute_num.append(abs(num))
# print(absolute_num)
# # [3, 1, 0, 10, 20, 5]
# print(all_nums)
# # [-3, 1, 0, 10, -20, 5]    # родительская последовательность отается не тронутой.
# -------------------------------------------------------------------------------------

# -сформируем новый список (абсолютных значений) в сокращенном варианте for in:

# all_nums = [-3, 1, 0, 10, -20, 5]
# absolute_num = [abs(num) for num in all_nums]

# print(absolute_num)
# # [3, 1, 0, 10, 20, 5]
# print(all_nums)
# # [-3, 1, 0, 10, -20, 5]
# --------------------------------------------------------------------------------------

# Пример 2:
# -сформируем новый позитивный список (с фильтрацией) в обычном for in:

# all_nums = [-3, 1, 0, 10, -20, 5]
# positive_nums = []

# for num in all_nums:
#     if num > 0:
#         positive_nums.append(num)
# print(positive_nums)
# # [1, 10, 5]
# print(all_nums)
# # [-3, 1, 0, 10, -20, 5]

# -сформируем новый позитивный список (с фильтрацией) в сокращенном варианте for in:

# all_nums = [-3, 1, 0, 10, -20, 5]
# positive_nums = [num for num in all_nums if num > 0]

# print(positive_nums)
# # [1, 10, 5]
# print(all_nums)
# # [-3, 1, 0, 10, -20, 5]
# ------------------------------------------------------------

# Пример 3: (элементы нового набора это квадрат элементов существующего)
# - сформируем новый набор (множество) в обычном for in:

# my_set = {1, 10, 15}
# new_set = set()

# for num in my_set:
#     new_set.add(num * num)
# print(new_set)
# # {1, 100, 225}
# print(my_set)
# # {1, 10, 15}

# - в сокращенном варианте for in:

# my_set = {1, 10, 15}
# new_set = {num * num for num in my_set}

# print(new_set)
# # {1, 100, 225}
# print(my_set)
# # {1, 10, 15}


# Пример 4: (значения в словаре должны быть увеличены в 10 раз)
# - в обычном for in:

# my_dict = {
#     'a':10,
#     "b": 7,
#     'd': 14
#     }

# new_dict = {}
# for k, v in my_dict.items():
#     new_dict[k] = v * 10
# print(new_dict)
# # {'a': 100, 'b': 70, 'd': 140}
# print(my_dict)
# # {'a': 10, 'b': 7, 'd': 14}

# - в сокращённом for in:
# my_dict = {
#     'a':10,
#     "b": 7,
#     'd': 14
#     }

# new_dict = {k: (v * 10) for k, v in my_dict.items()}

# print(new_dict)
# # {'a': 100, 'b': 70, 'd': 140}
# print(my_dict)
# # {'a': 10, 'b': 7, 'd': 14}


# Практика:

# из сдловарей можно фрмировать не только словари но наборы(множества). Для этого в строке 942 вместо выражения (ключ: значение) необходимо оставить только выражение относящееся к (значению). Результат в строке 945, а в строке 947 показан класс set - наборы(множества).

# my_dict = {
#     'a':10,
#     "b": 7,
#     'd': 14
#     }

# new_dict = {(v * 10) for k, v in my_dict.items()}

# print(new_dict)
# # {140, 100, 70}
# print(type(new_dict))
# # <class 'set'>
# print(my_dict)
# # {'a': 10, 'b': 7, 'd': 14}
# -----------------------------------------------


# Встает вопрос: в можно ли из списка сформировать словарь?

# my_scores = [10, 7, 14]

# # my_dict = {     # такой словарь мы хотим получить
# #     '0':10,
# #     '1': 7,
# #     '2': 14
# #     }

# scores = {index: elem for index, elem in enumerate(my_scores)}
# print(scores)
# # {0: 10, 1: 7, 2: 14}     # ну вот и поучили
# ------------------------------------------------


# Задача 1.
# 1. создайте словарь с несколькими ключами, значкния которых должны быть типа <str>.
# 2. создайто новый словарь на основании существуюшего, значения всех ключей должны быть в верхнем регистре.
# 3. вывести в терминал полученный словарь

# your_dict = {'first': "Julia",
#              'second': 'Tom',
#              'third': 'Bob'}

# my_dict = {k: v.upper() for k, v in your_dict.items()}
# print(my_dict)
# # {'first': 'JULIA', 'second': 'TOM', 'third': 'BOB'}


# Задача 2.
# 1. создать список с элементами типа сторока
# 2. создать новый список со строками длины которых больше трёх.
# 3. вывести в терминал

# your_list = ['Julia', 'Tom', 'Bob', 'Alice']
# my_list = [elem for elem in your_list if len(elem) > 3]
# print(my_list)
# # ['Julia', 'Alice']

# your_list = ['Julia', 'Tom', 'Bob', 'Alice']
# my_list = []
# for elem in your_list:
#     if len(elem) > 3:
#         my_list.append(elem)
# print(my_list)
# # ['Julia', 'Alice']
