
# СПИСКИ

# Список (list) представляет тип данных, который хранит набор или последовательность элементов. Во многих языках программирования есть аналогичная структура данных, которая называется массив.
# Для создания списка применяются квадратные скобки [], внутри которых через запятую перечисляются элементы списка. Например, определим список чисел:

# numbers = [1, 2, 3, 4, 5]

# Подобным образом можно определять списки с данными других типов, например, определим список строк:

# people = ["Tom", "Sam", "Bob"]

# Также для создания списка можно использовать функцию-конструктор list():

# numbers1 = []
# numbers2 = list()

# Оба этих определения списка аналогичны - они создают пустой список.

# Список необязательно должен содержать только однотипные объекты. Мы можем поместить в один и тот же список одновременно строки, числа, объекты других типов данных:

# objects = [1, 2.6, "Hello", True]

# Для проверки элементов списка можно использовать стандартную функцию print, которая выводит содержимое списка в удобочитаемом виде:

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# # [1, 2, 3, 4, 5]

# people = ["Tom", "Sam", "Bob"]
# print(people)
# # ['Tom', 'Sam', 'Bob']

# Конструктор list может принимать набор значений, на основе которых создается список:

# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = list(numbers1)
# print(numbers2)
# # [1, 2, 3, 4, 5]

# letters = list('Hello')
# print(letters)
# # ['H', 'e', 'l', 'l', 'o']

# Если необходимо создать список, в котором повторяется одно и то же значение несколько раз, то можно использовать символ звездочки *, то есть фактически применить операцию умножения к уже существующему списку:

# numbers = [5] * 6
# print(numbers)
# # [5, 5, 5, 5, 5, 5]
# people = ['Tom'] * 3
# print(people)
# # ['Tom', 'Tom', 'Tom']
# students = ['Sam', 'Bob'] * 2
# print(students)
# # ['Sam', 'Bob', 'Sam', 'Bob']

# ОБРАЩЕНИЕ К ЭЛЕМЕНТАМ СПИСКА

# Для обращения к элементам списка надо использовать индексы, которые представляют номер элемента в списка. Индексы начинаются с нуля. То есть первый элемент будет иметь индекс 0, второй элемент - индекс 1 и так далее. Для обращения к элементам с конца можно использовать отрицательные индексы, начиная с -1. То есть у последнего элемента будет индекс -1, у предпоследнего - -2 и так далее.

# people = ["Tom", "Sam", "Bob"]
# получение элементов с начала списка

# print(people[0])    # Tom
# print(people[1])    # Sam
# print(people[2])    # Bob

# # получение элементов с конца списка
# print(people[-2])   # Sam
# print(people[-1])   # Bob
# print(people[-3])   # Tom

# Для изменения элемента списка достаточно присвоить ему новое значение:

# people = ["Tom", "Sam", "Bob"]

# people[1] = "Mike"  # изменение второго элемента
# print(people[1])    # Mike
# print(people)       # ["Tom", "Mike", "Bob"]



# РАЗЛОЖЕНИЕ СПИСКА

# Python позволяет разложить список на отдельные элементы:

# people = ["Tom", "Bob", "Sam"]
# tom, bob, sam = people

# print(tom)       # Tom
# print(bob)       # Bob
# print(sam)       # Sam

# В данном случае переменным tom, bob и sam последовательно присваиваются элементы из списка people. Однако следует учитывать, что количество переменных должно быть равно числу элементов присваиваемого списка.

# ПЕРЕБОР ЭЛЕМЕНТОВ

# Для перебора элементов можно использовать как цикл for, так и цикл while.

# Перебор с помощью цикла for:

# people = ["Tom", "Sam", "Bob"]
# for person in people:
#     print(person)
# # Tom
# # Sam
# # Bob
# Здесь будет производиться перебор списка people, и каждый его элемент будет помещаться в переменную person.

# Перебор также можно сделать с помощью цикла while:

# people = ["Tom", "Sam", "Bob"]
# i = 0
# while i < len(people):
#     print(people[i])     # применяем индекс для получения элемента
#     i += 1
# # Tom
# # Sam
# # Bob
# Для перебора с помощью функции len() получаем длину списка. С помощью счетчика i выводит по элементу, пока значение счетчика не станет равно длине списка.



# СРАВНЕНИЕ СПИСКОВ

# Два списка считаются равными, если они содержат один и тот же набор элементов:

# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = list([1, 2, 3, 4, 5])
# if numbers1 == numbers2:
#     print("numbers1 equal to numbers2")
# else:
#     print("numbers1 is not equal to numbers2")
# # numbers1 equal to numbers2



# ПОЛУЧЕНИЕ ЧАСТИ СПИСКА

# Если необходимо получить какую-то определенную часть списка, то мы можем применять специальный синтаксис, который может принимать следующие формы:

# list[:end]: через параметр end передается индекс элемента, до которого нужно копировать список

# list[start:end]: параметр start указывает на индекс элемента, начиная с которого надо скопировать элементы

# list[start:end:step]: параметр step указывает на шаг, через который будут копироваться элементы из списка. По умолчанию этот параметр равен 1.

# people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]

# slice_people1 = people[:3]   # с 0 по 3
# print(slice_people1)     # ["Tom", "Bob", "Alice"]

# slice_people2 = people[1:3]   # с 1 по 3
# print(slice_people2)   # ["Bob", "Alice"]

# slice_people3 = people[1:6:2]   # с 1 по 6 с шагом 2
# print(slice_people3)   # ["Bob", "Sam", "Bill"]

# Можно использовать отрицательные индексы, тогда отсчет будет идти с конца, например, -1 - предпоследний, -2 - третий сконца и так далее.

# people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]

# slice_people1 = people[:-1]   # с предпоследнего по нулевой
# print(slice_people1)
# # ["Tom", "Bob", "Alice", "Sam", "Tim"]
# slice_people2 = people[-3:-1]   # с третьего с конца по предпоследний
# print(slice_people2)
# [ "Sam", "Tim"]




# МЕТОДЫ И ФУНКЦИИ ПО РАБОТЕ СO СПИСКАМИ:

# append(item): добавляет элемент item в конец списка

# insert(index, item): добавляет элемент item в список по индексу index

# extend([items]): добавляет набор элементов items в конец списка

# remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError

# clear(): удаление всех элементов из списка

# index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError

# pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.

# count(item): возвращает количество вхождений элемента item в список

# sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.

# reverse(): расставляет все элементы в списке в обратном порядке

# copy(): копирует список

# # Кроме того, Python предоставляет ряд встроенных функций для работы со списками:

# len(list): возвращает длину списка

# sorted(list, [key]): возвращает отсортированный список

# min(list): возвращает наименьший элемент списка

# max(list): возвращает наибольший элемент списка

# ---------------------------------------------------------------------------

# dict.fromkeys() этот Метод в Python является удобным способом создать словарь, где ключи — это элементы из заданного итерируемого объекта (например, списка или кортежа), а значения для всех этих ключей будут одинаковыми. Этот метод также можно использовать для удаления дубликатов из списка, сохраняя при этом порядок элементов.
# Пример использования
# Давайте рассмотрим, как использовать dict.fromkeys() для удаления дубликатов из списка:

# my_list = [1, 2, 2, 3, 4, 4, 5]  

# # Создаем словарь с ключами из my_list и значением None  
# unique_dict = dict.fromkeys(my_list)  

# # Переводим ключи словаря обратно в список  
# unique_list = list(unique_dict)  

# print(unique_list)  # Вывод: [1, 2, 3, 4, 5]  

# Как это работает:
# Создание словаря: Когда вы передаете список my_list в dict.fromkeys(), создается словарь, где каждый уникальный элемент списка становится ключом, а значением будет None (или другое значение, если оно указано).

# Сохранение порядка: Словари в Python 3.7 и выше сохраняют порядок добавления элементов. Поэтому, когда вы переводите уникальные ключи обратно в список, порядок оригинальных элементов сохраняется.

# Преимущества: Этот метод прост и эффектив, особенно если порядок важен. В отличие от преобразования списка в set, который не сохраняет порядок, dict.fromkeys() позволяет сохранить порядок появления элементов.
# ------------------------------------------------------------------------------

# Чтобы исключить дубликаты из списка в Python, вы можете использовать несколько подходов. Вот несколько простых способов:

# 1. Использование set
# Самый простой способ — преобразовать список в set, который автоматически уберёт все дубликаты:

# my_list = [1, 2, 2, 3, 4, 4, 5]  
# unique_list = list(set(my_list))  
# print(unique_list)  # Вывод: [1, 2, 3, 4, 5]  

# 2. Сохранение порядка с помощью dict.fromkeys()
# Если нужно сохранить порядок элементов, вы можете использовать метод dict.fromkeys():

# my_list = [1, 2, 2, 3, 4, 4, 5]  
# unique_list = list(dict.fromkeys(my_list))  
# print(unique_list)  # Вывод: [1, 2, 3, 4, 5]  

# 3. Использование списка и цикла
# Ещё один способ — использовать цикл и проверять наличие элемента в новом списке:

# my_list = [1, 2, 2, 3, 4, 4, 5]  
# unique_list = []  
# for item in my_list:  
#     if item not in unique_list:  
#         unique_list.append(item)  
# print(unique_list)  # Вывод: [1, 2, 3, 4, 5]  

# -----------------------------------------------------------------------------


# ИСПОЛЬЗОВАНИЕ МЕТОДОВ:

# people = ['Tom', 'Bob']

# # # добавляем в конец списка
# people.append("Alice")
# print(people)
# # ['Tom', 'Bob', 'Alice']

# # добавляем на вторую позицию
# people.insert(1, 'Bill')
# print(people)
# # ['Tom', 'Bill', 'Bob', 'Alice']

# # добавляем набор элементов ["Mike", "Sam"]
# people.extend(['Mike', 'Sam'])
# print(people)
# # ['Tom', 'Bill', 'Bob', 'Alice', 'Mike', 'Sam']

# # получаем индекс элемента
# index_of_tom = people.index('Tom')
# # удаляем по этому индексу
# removed_item = people.pop(index_of_tom)
# print(people)
# # ['Bill', 'Bob', 'Alice', 'Mike', 'Sam']

# # удаляем последний элемент
# last_item = people.pop()
# print(people)
# # ['Bill', 'Bob', 'Alice', 'Mike']

# # удаляем элемент "Alice"
# people.remove('Alice')
# print(people)
# # ['Bill', 'Bob', 'Mike']

# # удаляем все элементы:
# people.clear()
# print(people)
# # []


# ПРОВЕРКА НАЛИЧИЯ ЭЛЕМЕНТА:

# Если определенный элемент не найден, то методы remove и index генерируют исключение. Чтобы избежать подобной ситуации, перед операцией с элементом можно проверять его наличие с помощью ключевого слова in:

# people = ["Tom", "Bob", "Alice", "Sam"]

# if "Alice" in people:
#     people.remove("Alice")
# print(people)
# # ["Tom", "Bob", "Sam"]

# Выражение if "Alice" in people возвращает True, если элемент "Alice" имеется в списке people. Поэтому конструкция if "Alice" in people может выполнить последующий блок инструкций в зависимости от наличия элемента в списке.

# УДАЛЕНИЕ С ПОМОЩЬЮ del

# Python также поддерживает еще один способ удаления элементов списка - с помощью оператора del. В качестве параметра этому оператору передается удаляемый элемент или набор элементов:

# people = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]

# del people[1]   # удаляем второй элемент
# print(people)   # ["Tom", "Alice", "Sam", "Bill", "Kate", "Mike"]
# del people[:3]   # удаляем  по четвертый элемент не включая
# print(people)   # ["Bill", "Kate", "Mike"]
# del people[1:]   # удаляем  со второго элемента
# print(people)   # ["Bill"]


# ИЗМЕНЕНИЕ ПОДСПИСКА:

# Для изменения подсписка - набора элементов в списке можно использовать вышерассмотренный синтаксис [start:end]:

# nums = [10, 20, 30, 40, 50]
# nums[1:4]=[11, 22]
# print(nums)    # [10, 11, 22, 50]

# Здесь выражение nums[1:4] фактически обращается к подсписку [20, 30, 40]. Присвоение этому подсписку списка [11, 22] позволяет заменить элементы списка nums на новые. И после изменения получим список [10, 11, 22, 50].


# ПОДСЧЕТ ВХОЖДЕНИЙ:

# Если необходимо узнать, сколько раз в списке присутствует тот или иной элемент, то можно применить метод count():

# people = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]

# people_count = people.count("Tom")
# print(people_count)  # 3


# СОРТИРОВКА:

# Для сортировки по возрастанию применяется метод sort():

# people = ["Tom", "Bob", "Alice", "Sam", "Bill"]

# people.sort()
# print(people)    # ["Alice", "Bill", "Bob", "Sam", "Tom"]

# # Если необходимо отсортировать данные в обратном порядке, то мы можем после сортировки применить метод reverse():
# people.reverse()
# print(people)    # ['Tom', 'Sam', 'Bob', 'Bill', 'Alice']

# При сортировке фактически сравниваются два объекта, и который из них "меньше", ставится перед тем, который "больше". Понятия "больше" и "меньше" довольно условны. И если для чисел все просто - числа расставляются в порядке возрастания, то для строк и других объектов ситуация сложнее. В частности, строки оцениваются по первым символам. Если первые символы равны, оцениваются вторые символы и так далее. При чем цифровой символ считается "меньше", чем алфавитный заглавный символ, а заглавный символ считается меньше, чем строчный.

# Таким образом, если в списке сочетаются строки с верхним и нижним регистром, то мы можем получить не совсем корректные результаты, так как для нас строка "bob" должна стоять до строки "Tom". И чтобы изменить стандартное поведение сортировки, мы можем передать в метод sort() в качестве параметра функцию:

# people = ["Tom", "bob", "alice", "Sam", "Bill"]

# people.sort()    # стандартная сортировка
# print(people)    # ["Bill", "Sam", "Tom", "alice", "bob"]

# people.sort(key=str.lower) # сортировка без учета регистра
# print(people)    # ["alice", "Bill", "bob", "Sam", "Tom"]

# Кроме метода sort мы можем использовать встроенную функцию sorted, которая имеет две формы:
# sorted(list): сортирует список list
# sorted(list, key): сортирует список list, применяя к элементам функцию key

# people = ["Tom", "bob", "alice", "Sam", "Bill"]

# sorted_people = sorted(people, key=str.lower)
# print(sorted_people)     # ["alice", "Bill", "bob", "Sam", "Tom"]

# При использовании этой функции следует учитывать, что эта функция не изменяет сортируемый список, а все отсортированные элементы она помещает в новый список, который возвращается в качестве результата.


# ФИЛЬТРОЦИЯ СПИСКА:
# Для фильтрации списка применяется функция filter(), в которую передается функция-условие и фильтруемый список:

# filter(fun, iter)

# Функция принимает два параметра:

# fun: функция-условие, в которую передается каждый элемент коллекции и которая возвращает True, если элемент соответствует условию. Иначе возвращается False.
# iter: фильтруемая коллекция

# В качестве результата функция возвращает отфильтрованные элементы. Например, получим из списка чисел все значения больше 1:

# numbers = [-2, -1, 0, 1, 2, 3, 4]

# def condition(number):
#     return number > 1

# result = filter(condition, numbers)

# for n in result:
#     print(n, end=" ")   # 2 3 4

# Здесь фильтруется список numbers. Для фильтрации определяем функцию condition, в которую в качестве параметра передается каждый элемент списка numbers. Результатом функции являет True, если число больше 1, либо False, если число меньше 2.
# Результатом функции filter является отфильтрованные значения из списка, то есть те числа, которые больше 1.

# Вместо определения отдельной функции-условия, если условие короткое, удобно в подобных случаях использовать лямбда-выражения:

# numbers = [-2, -1, 0, 1, 2, 3, 4]

# result = filter(lambda n: n > 1, numbers)

# for n in result:
#     print(n, end=" ")    # 2 3 4

# Аналогичным образом можно отфильтровать списки более сложных объектов:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# people = [ Person("Tom", 38), Person("Kate", 31), Person("Bob", 42),
#         Person("Alice", 34), Person("Sam", 25) ]

# # фильтрация элементов, у которых age > 33
# view = filter(lambda p: p.age > 33, people)

# for person in view:
#     print(f"Name: {person.name} Age: {person.age}")
# # Name: Tom Age: 38
# # Name: Bob Age: 42
# # Name: Alice Age: 34

# В данном случае фильтруем список объектов Person, поэтому в функцию-условие/лямбда-выражение в качестве параметра передается каждый объект Person из списка. Каждый объект Person хранит имя (Name) и возраст (Age), и здесь выбираем всех Person, у которых возраст больше 33.


# ПРОЕКЦИЯ СПИСКА:

# Для проекции/преобразования элементов списка применяется функция map(), в которую передается функция-условие и список, элементы которого надо преобразовать:

# map(fun, iter)

# Функция принимает два параметра:

# fun: функция преобразования, в которую передается каждый элемент коллекции.
# iter: перебираемая коллекция

# Из результата функции мы получим преобразованные элементы списка. Например, преобразуем список чисел в квадраты этих чисел:

# numbers = [ 1, 2, 3, 4, 5]

# def square(number):
#     return number * number

# result = map(square, numbers)
# for n in result:
#     print(n, end=" ")   # 1 4 9 16 25

# В качестве функции преобразования здесь выступает функция square, в которую передается число из списка и которая возвращает его квадрат.

# Также в качестве функции преобразования можно использовать лямбда-выражения:

# numbers = [ 1, 2, 3, 4, 5]

# result = map(lambda n:
#     n * n, numbers)
# for n in result:
#     print(n, end=" ")   # 1 4 9 16 25

# Аналогичным образом можно преобразовывать коллекции более сложных объектов:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# people = [ Person("Tom", 38), Person("Kate", 31), Person("Bob", 42),
#         Person("Alice", 34), Person("Sam", 25) ]

# # получаем из Person строку с именем
# view = map(lambda p:
#     p.name, people)

# for person in view:
#     print(person, end=' ')  # Tom Kate Bob Alice Sam

# Здесь проекция применяется к списку объектов Person. Функция 'преобразование' получает каждый объект Person и возвращает значение его атрибута name. То есть в результате мы получим набор строк (атрибуты name всех объектов Person).


# МИНИМАЛЬНОЕ И МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ

# Встроенный функции Python min() и max() позволяют найти минимальное и максимальное значения соответственно:

# numbers = [9, 21, 12, 1, 3, 15, 18]
# print(min(numbers))     # 1
# print(max(numbers))     # 21


# КОПИРОВАНИЕ СПИСКОВ

# При копировании списков следует учитывать, что списки представляют изменяемый (mutable) тип, поэтому если обе переменных будут указывать на один и тот же список, то изменение одной переменной, затронет и другую переменную:

# people1 = ["Tom", "Bob", "Alice"]
# people2 = people1
# people2.append("Sam")    # добавляем элемент во второй список
# # people1 и people2 указывают на один и тот же список
# print(people1)   # ["Tom", "Bob", "Alice", "Sam"]
# print(people2)   # ["Tom", "Bob", "Alice", "Sam"]

# И чтобы происходило копирование элементов, но при этом переменные указывали на разные списки, можно использовать метод copy():

# people1 = ["Tom", "Bob", "Alice"]
# people2 = people1.copy()     # копируем элементы из people1 в people2
# people2.append("Sam")        # добавляем элемент ТОЛЬКО во второй список
# # people1 и people2 указывают на разные списки
# print(people1)   # ["Tom", "Bob", "Alice"]
# print(people2)   # ["Tom", "Bob", "Alice", "Sam"]


# СОЕДИНЕНИЕ СПИСКОВ
# Для объединения списков применяется операция сложения (+):

# people = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]

# print(people[0])         # ["Tom", 29]
# print(people[0][0])      # Tom
# print(people[0][1])      # 29

# Чтобы обратиться к элементу вложенного списка, необходимо использовать пару индексов: people[0][1] - обращение ко второму элементу первого вложенного списка.

# Добавление, удаление и изменение общего списка, а также вложенных списков аналогично тому, как это делается с обычными (одномерными) списками:

# people = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]

# # создание вложенного списка
# person = list()
# person.append("Bill")
# person.append(41)
# # добавление вложенного списка
# people.append(person)

# print(people[-1])        # ["Bill", 41]

# # добавление во вложенный список
# people[-1].append("+79876543210")

# print(people[-1])        # ["Bill", 41, "+79876543210"]

# # удаление последнего элемента из вложенного списка
# people[-1].pop()
# print(people[-1])        # ["Bill", 41]

# # удаление всего последнего вложенного списка
# people.pop(-1)

# # изменение первого элемента
# people[0] = ["Sam", 18]
# print(people)            # [ ["Sam", 18], ["Alice", 33], ["Bob", 27]]

# Перебор вложенных списков:

# people = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]

# for person in people:
#     for item in person:
#         print(item, end="|")   # Tom|29|Alice|33|Bob|27|


# СПИСКИ И АЛГОРИТМЫ

# Списки нередко используются для решения различных задач, в которых, на первый взгляд, в применении списков нет смысла, тем не менее списки позволяют упростить написание алгоритма, либо просто предоставить альтернативное решение. Например, возьмем задачу по нахождению факториала числа:

# fact = lambda n: [1,0] [n>1] or fact(n-1) * n
# print(fact(4))   # 24

# Для вычисления факториала здесь определена переменная fact, которая хранит лямбда-выражение. Рассмотрим его по частям. Вначале идет определение списка из двух элементов:

# [1,0]
# Дальше идет обращение к элементу списка с помощью индекса:

# [1,0] [n>1]
# Здесь результат выражения n>1 и будет представлять индекс в списке. То есть, если аргумент лямбда-выражения n больше 1, то выражение n>1 равно True или 1, а все выражение [1,0] [n>1] возвратит 0 (элемент по индексу 1). Если же n равно или меньше 1, то выражение n>1 равно False или 0, а все выражение [1,0] [n>1] возвратит 1 (элемент по индексу 0)

# Дальше идет оператор or. Если выражение [1,0] [n>1] возвратит 1 (в случае если n<=1), то оператор or возвращает это число 1. Если же выражение [1,0] [n>1] возвратит 0 (в случае если n>1), то оператор or возвращает результат выражения fact(n-1) * n, которое рекурсивно вызывает функцию fact, передавая в нее число n-1. В итоге, если n=4, мы получим следующую последовательность действий:

# [1,0] [4>1] or fact(4-1) * 4

# 0 or fact(4-1) * 4

# ([1,0] [3>1] or fact(3-1)) * 4

# (0 or fact(3-1)) * 4

# (([1,0] [2>1] or fact(2-1)) * 3) * 4

# ((0 or fact(2-1)) * 3) * 4

# ((([1,0] [1>1] or fact(1-1)) * 2) * 3) * 4

# (((1 or fact(1-1)) * 2) * 3) * 4

# (((1) * 2) * 3) * 4
