# Упражнение 110. Порядок сортировки

# Напишите программу, которая будет запрашивать у пользователя целочисленные значения и сохранять их в виде списка. Индикатором окончания ввода значений должен служить ноль. Затем программа должна вывести на экран все введенные пользователем числа (кроме нуля) в порядке возрастания – по одному значению в строке. Используйте для сортировки либо метод sort, либо функцию sorted.

# data = []

# num = int(input("Введите целое число (0 для окончания ввода): "))
# while num != 0:
#     data.append(num)
#     num = int(input("Введите целое число (0 для окончания ввода): "))

# print(data)
# data.sort()
# print(data)
# print("Введенные числа в порядке возрастания: ")
# for num in data:
#     print(num, end=' ')


# Упражнение 111. Обратный порядок

# Напишите программу, которая, как и в предыдущем случае, будет запрашивать у пользователя целые числа и сохранять их в виде списка. Индикатором окончания ввода значений также должен служить ноль. На этот раз необходимо вывести на экран введенные значения в порядке убывания.

# data = []
# num = int(input("Введите целое число (0 для окончания ввода): "))

# while num != 0:
#     data.append(num)
#     num = int(input("Введите целое число (0 для окончания ввода): "))

# data.sort()
# print(data)
# data.reverse()
# print(data)

# for num in data:
#     print(num, end=' ')


# Упражнение 112. Удаляем выбросы (data processing)

# При анализе собранных по результатам научных экспериментов данных зачастую возникает необходимость избавиться от экстремальных значений, прежде чем продолжать двигаться дальше. Напишите функцию, создающую копию списка с исключенными из него n наибольшими и наименьшими значениями и возвращающую ее в качестве результата. Порядок следования элементов в измененном списке не обязательно должен в точности совпадать с источником.
# В основной программе должна быть продемонстрирована работа вашей функции. Для начала попросите пользователя ввести целые числа, затем соберите их в список и вызовите написанную вами ранее функцию. Выведите на экран измененную версию списка вместе с оригинальной. Если пользователь введет менее четырех чисел, должно быть отображено соответствующее сообщение об ошибке.


# data = []

# num = int(input("Введите целое число (0 для окончания ввода): "))
# while num != 0:
#     data.append(num)
#     num = int(input("Введите целое число (0 для окончания ввода): "))

# while len(data) <= 4:
#     num = int(input("Введите целое число (0 для окончания ввода): "))
#     data.append(num)
# print(data)

# my_set = set(data)
# data = list(my_set)
# data.sort()
# print(data)

# data.pop()
# data.pop(0)
# print(data)


# Упражнение 113. Избавляемся от дубликатов

# В данном упражнении вам предстоит разработать программу, в которой у пользователя будет запрошен список слов, пока он не оставит строку ввода пустой. После этого на экране должны быть показаны слова, введенные пользователем, но без повторов, – каждое по одному разу. При этом слова должны быть отображены в том же порядке, в каком их вводили с клавиатуры. Например, если пользователь на запрос программы введет следующий список слов:
# first
# second
# first
# third
# second
# программа должна вывести:
# first
# second
# third

# data = []

# word = input('Введите слово (всего их потребуется пять. B конце нажмите Enter): ')
# while word != "":
#     data.append(word)
#     word = input('Введите слово (всего их потребуется пять. B конце нажмите Enter): ')

# data = list(dict.fromkeys(data))
# print(data)
# for item in data:
#     print(item)
# # все работает

# Упражнение 114. Отрицательные, положительные и нули.

# Напишите программу, запрашивающую у пользователя целые числа, пока он не оставит строку ввода пустой. После окончания ввода на экран должны быть выведены сначала все отрицательные числа, которые были введены, затем нулевые и только после этого положительные. Внутри каждой группы числа должны отображаться в той последовательности, в которой были введены пользователем. Например, если он ввел следующие числа: 3, -4, 1, 0, -1, 0 и -2, вывод должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1.Каждое значение должно отображаться на новой строке.

# data1 = []
# data2 = []
# data3 = []
# # ввел 9, 7, -5, -6, 0, 3, -1, 0
# line = input("Введите целое число (Enter для окончания ввода): ")

# while line != "":
#     num = int(line)
#     if num < 0:
#         data1.append(num)
#     elif num > 0:
#         data3.append(num)
#     else:
#         data2.append(num)

#     num = line = input("Введите целое число (Enter для окончания ввода): ")

# data = data1 + data2 + data3
# for item in data:
#     print(item, end=' ') # -5 -6 -1 0 0 9 7 3


# Упражнение 115. Список собственных делителей

# Собственным делителем числа называется всякий его делитель, отличный от самого числа. Напишите функцию, которая будет возвращать список всех собственных делителей заданного числа. Само это число должно передаваться в функцию в виде единственного аргумента. Результатом функции будет перечень собственных делителей числа, собранных в список. Основная программа должна демонстрировать работу функции, запрашивая у пользователя число и выводя на экран список его собственных делителей. Программа должна запускаться только в том случае, если она не импортирована в виде модуля в другой файл.

# def main():
#     num = int(input("Введите целое число: "))
#     properDivisors(num)

# def properDivisors(num):
#     divisors = []
#     n = list(range(1, num))
#     for i in n:
#         if num % i == 0:
#             divisors.append(i)
#     print(divisors)
# main()

# Ваш код можно улучшить как с точки зрения эффективности, так и с точки зрения стиля. Приведённый ниже код имеет улучшения, включая использование списка списков и генераторов, а также более ясные имена функций. Кроме того, проверку на целочисленность можно сделать при помощи обработки исключений для обеспечения корректного ввода:

# def main():
#     try:
#         num = int(input("Введите целое число: "))
#         divisors = find_proper_divisors(num)
#         print("Делители:", divisors)
#     except ValueError:
#         print("Пожалуйста, введите корректное целое число.")

# def find_proper_divisors(num):
#     return [i for i in range(1, num) if num % i == 0]

# if __name__ == "__main__":
#     main()

# Изменения и улучшения:

# 1. Именование функций: Я изменил имя функции properDivisors на find_proper_divisors, чтобы лучше отражать её назначение.

# 2. Использование генераторов списков: Это упрощает код и может повысить производительность, особенно при больших числах.

# 3. Обработка ошибок: Добавление обработки исключений позволяет избежать сбоев, если пользователь введёт неправильный тип данных.

# 4. Основная точка входа: Проверка if __name__ == "__main__": позволяет использовать функцию main и в качестве исполняемого скрипта, и в качестве импортируемого модуля.


# Упражнение 116. Совершенные числа

# Целое число n называется совершенным, если сумма всех его собственных делителей равна самому числу n. Например, 28 – это совершенное число, поскольку его собственными делителями являются 1, 2, 4, 7 и 14, а 1 + 2+ 4 + 7 + 14 = 28.
# Напишите функцию для определения того, является ли заданное число совершенным. Функция будет принимать на вход единственный параметр и возвращать True, если он представляет собой совершенное число, и False – если нет. Разработайте небольшую программу, которая будет использовать функцию для идентификации и вывода на экран всех совершенных чисел в диапазоне от 1 до 10 000. При решении этой задачи импортируйте функцию, написанную в упражнении 115.

# Вот программа на Python, которая использует функцию для идентификации и вывода всех совершенных чисел в диапазоне от 1 до 1000:


# def is_perfect_number(num):
#     """Проверяет, является ли число совершенным."""
#     if num < 1:
#         return False
#     divisors_sum = sum(i for i in range(1, num) if num % i == 0)
#     return divisors_sum == num

# def find_perfect_numbers(limit):
#     """Ищет все совершенные числа в заданном диапазоне."""
#     perfect_numbers = []
#     for i in range(1, limit + 1):
#         if is_perfect_number(i):
#             perfect_numbers.append(i)
#     return perfect_numbers

# def main():
#     limit = 1000
#     perfect_numbers = find_perfect_numbers(limit)
#     print(f"Совершенные числа в диапазоне от 1 до {limit}: {perfect_numbers}")

# if __name__ == "__main__":
#     main()


# Как работает код:
# 1. Функция `is_perfect_number(num) - Принимает целое число и вычисляет сумму его делителей (исключая само число).
# - Возвращает `True`, если сумма делителей равна числу, иначе — `False`.

# 2. Функция `find_perfect_numbers(limit)`:
# - Перебирает числа от 1 до заданного лимита.
# - Использует `is_perfect_number()` для проверки, является ли каждое число совершенным.
# - Возвращает список всех совершенных чисел.

# 3. Функция `main()`:
# - Определяет лимит, вызывает функцию для поиска совершенных чисел и выводит их на экран.

# Результат:
# Когда вы запустите эту программу, она выведет все совершенные числа в диапазоне от 1 до 1000. Совершенные числа в этом диапазоне: **6, 28, 496**.
# -------------------------------------------------------------------------------

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

# fruit_num_dict = dict(fruit_num_zip)
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
