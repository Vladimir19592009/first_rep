# МНОЖЕСТВА
# - это объект-контейнер уникальных значений,
# который работает как мате­матическое множество.

# + Все элементы в множестве должны быть уникальными. Никакие два элемента
# +не мoryr иметь одинаковое значение.

# + Множества не упорядочены, т. е. элементы в множестве не хранятся в каком-то
# +опреде­ленном порядке.

# + Хранящиеся в множестве элементы могут иметь разные типы данных.

# СОЗДАНИЕ МНОЖЕСТВА
# Для того чтобы создать множество, необходимо вызвать встроенную функцию set.
# Вот пример создания пустого множества:

# переменная = set()

# После исполнения этой инструкции переменная myset будет ссылаться на пустое множество.
# В функцию set можно также передать один аргумент. Передаваемый аргумент должен быть объектом,
# который содержит итерируемые элементы, такие как список, кортеж или строко­вое значение.
# Отдельные элементы объекта, передаваемого в качестве аргумента, становятся
# элементами множества.

# myset = set(['а', 'б', 'в'])
# В этом примере в функцию set в качестве аргумента передается список.
# После исполнения этой инструкции переменная myset ссылается на множество,
# содержащее элементы 'а', 'б', 'в'.

# Если в качестве аргумента в функцию set передать строковое значение,
# то каждый отдель­ный символ в строковом значении становится членом множества.

# myset = set('абв')

# После исполнения этой инструкции переменная myset будет ссылаться на множество,
# содержащее элементы 'а', 'б', 'в'.

# Множества не могут содержать повторяющиеся элементы. Если в функцию set передать
# аргумент, содержащий повторяющиеся элементы, то в множестве появится только один
# из этих повторяющихся элементов.

# myset = sеt('ааабв')

# Символ 'а' встречается в строковом значении многократно, но в множестве он появится
# только один раз. После исполнения этой инструкции переменная myset будет ссылаться
# на множество, содержащее элементы 'а', 'б', 'в'.

# как создать множество с элемен­тами 'один', 'два' и 'три', ведь в функцию set можно
# передавать не более одного аргумента?
#  Для того чтобы создать множество, которое нам требуется,
# необходимо в качестве аргумента в функцию set передать список,
# содержащий строковые значения: ['один', 'два' и 'три'].
# Вот пример:

# myset = set(['один', 'два', 'три'])

# После исполнения этой инструкции переменная myset будет ссылаться на множество,
# со­держащее элементы 'один',' два', 'три' .

# ПОЛУЧЕНИЕ количества элементов в множестве

# Как и со списками, кортежами и словарями, функция len используется для получения
# количества элементов в множестве:

# myset = set([0, l, 2, 3, 4, 5])
# len(myset)
# 6


# ДОБАВЛЕНИЕ и УДАЛЕНИЕ элементов

# add()

# Множества являются мутируемыми объектами, поэтому элементы можно в них добавлять
# и удалять из них. Для добавления элемента в множество
# используется метод add().
'''
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
# {1, 2, 3}
myset.add(2) # такой элемент уже присутствует...
print(myset)
# {1, 2, 3}  результат тотже
'''

# update()

# В множество можно добавить сразу всю группу элементов при помощи метода update().
# При вызове метода update () в качестве аргумента передается объект, который содержит
# итерируемые элементы, такие как список, кортеж, строковое значение или другое множест­во.
# Отдельные элементы объекта, передаваемого в качестве аргумента,
# становятся элемен­тами множества.
'''
myset = set([1, 2, 3])
myset.update([4, 5, 6])
print(myset)
# {1, 2, 3, 4, 5, 6}
'''
# еще один пример:
'''
set1 = set([1, 2, 3])
set2 = set([8, 9, 10])
set1.update(set2)
print(set1)
print(set2)
# {1, 2, 3, 8, 9, 10}
# {8, 9, 10}
'''
# еще один пример:
'''
myset = set([1, 2, 3])
myset.update('abc')
print(myset)
# {1, 2, 3, 'b', 'a', 'c'}
'''
# или
'''
myset = set([1, 2, 3])
myset.update(['abc'])
print(myset)
# {1, 2, 3, 'abc'}
'''

# remove (), discard ()

# Элемент из множества можно удалить либо методом remove (), либо методом discard ().
# Удаляемый элемент передается в качестве аргумента в один из этих методов, и этот элемент
# удаляется из множества. Единственная разница между этими двумя методами состоит в том,
# как они себя ведут, когда указанный элемент в множестве не найден. Метод remove()
# вызывает исключение KeyError, а метод discard() исключение не вызывает.
'''
myset = set([1, 2, 3, 4, 5])
print(myset)
# {1, 2, 3, 4, 5}

myset.remove(1)
print(myset)
# {2, 3, 4, 5}

myset.discard(5)
print(myset)
# {2, 3, 4}

myset.discard(99)
print(myset)
# {2, 3, 4}

myset.remove(99)
print(myset)
# KeyError: 99
'''

# clear ()

# Все элементы множества можно удалить путем вызова метода clear () .
# Приведенный ниже интерактивный сеанс это демонстрирует:
'''
myset = set([1, 2, 3, 4, 5])
print(myset)
# {1, 2, 3, 4, 5}
myset.clear()
print(myset)
# set()
'''

# ЦИКЛ for
# Для последовательного перебора всех элементов в множестве
# цикл for используется в при­веденном ниже общем формате:

# for переменная in множество:
#   инструкция
#   инструкция

# В данном формате переменная - это имя переменной, множество - имя множества.
# Этот цикл делает одну итерацию для каждого элемента в множестве, во время которой
# перемен­ной присваивается элемент:
'''
myset = set(['a', 'b', 'c'])
for i in myset:
    print(i)
# b
# a
# c
'''

# ПРИМЕНЕНИЕ операторов

# in и not in

# Оператор in используется для определения, существует ли значение в множестве.
'''
myset = set(['a', 'b', 'c'])
if 'b' in myset:
    print('Leter b in')
# Leter b in
'''
'''
myset = set(['a', 'b', 'c'])
if 99 not in myset:
    print('Number is not in')
# Number is not in
'''

# ОБЪЕДИНЕНИЕ множеств

# (union () ИЛИ '|' )

# Объединение двух множеств - это операция, в результате которой получается
# множество, содержащее все элементы обоих множеств. В Python для получения
# объединения двух мно­жеств вызывается метод union ():

# множество1.uniоn(множество2)

# В данном формате множествоl и множество2 - это множества. Данный метод
# возвращает множество, в которое входят элементы множестваl и множества2.
'''
set1 = set([1, 2, 3, 4])
set2 = set([2, 4, 5, 8])
set3 = set1.union(set2)
print(set3)
# {1, 2, 3, 4, 5, 8} разумеется без повторов
'''
# Для объединения двух множеств можно также использовать оператор .
# Вот общий формат выражения с использованием оператора | с двумя множествами:

# множество1 | множество2
'''
set1 = set([1, 2, 3, 4])
set2 = set([2, 4, 5, 8])
set3 = set1 | set2
print(set3)
# {1, 2, 3, 4, 5, 8}
'''

# ПЕРЕСЕЧЕНИЕ множеств (intersection () ИЛИ &)

# Пересечение двух множеств - это операция над множествами, при которой в итоговое
# множество входят только те элементы, которые находятся в обоих множествах. В Python
# для получения пересечения двух множеств вызывается метод intersection ().

# множество1.intеrsесtiоn(множество2)

# Данный метод возвращает множество,в которое входят элементы, находящиеся одновременно
# в множествеl и в множестве2.
'''
set1 = set([1, 2, 3, 4])
set2 = set([2, 4, 5, 8])
set3 = set1.intersection(set2)
print(set3)
# {2, 4}
'''
# Для нахождения пересечения двух множеств можно также использовать оператор &.
# Вот общий формат выражения с использованием оператора ( & ) с двумя множествами:

# множество1 & множество2

# Здесь множествоl и множество2 - это множества.
# Данное выражение возвращает множество, в которое входят элементы,
# находящиеся одновременно в множествеl и в множестве2.
'''
set1 = set([1, 2, 3, 4])
set2 = set([2, 4, 5, 8])
set3 = set1 & set2
print(set3)
# {2, 4}
'''

# РАЗНОСТЬ множеств ( difference () ИЛИ ( - )минус)

# - это все элементы множестваl, не входящие в множество2. Для получения
# разности двух множеств вызывается метод difference ().

# множествоl.diffеrеnсе(множество2)
'''
set1 = set([1, 2, 3, 4])
set2 = set([2, 4, 5, 8])
set3 = set1.difference(set2)
print(set3)
# {1, 3}
'''
# множествоl - множество2
'''
set1 = set([1, 2, 3, 4])
set2 = set([2, 4, 5, 8])
set3 = set1 - set2
print(set3)
# {1, 3}
'''

# СИММЕТРИЧНАЯ разность множеств (symmetric_difference() или ( ^ ))

# Симметричная разность двух множеств - это множество, которое содержит элементы,
# непринадлежащие одновременно обоим исходным множествам. Иными словами, это
# элемен­ты, которые входят в одно из множеств, но не входят в оба множества одновременно.

# мнoжecтвol.syrnmetric_difference(мнoжecтвo2)
'''
set1 = set([1, 2, 3, 4])
set2 = set([2, 4, 5, 8])
set3 = set1.symmetric_difference(set2)
print(set3)
# {1, 3, 5, 8}
'''
# множествоl ^ множество2
'''
set1 = set([1, 2, 3, 4])
set2 = set([2, 4, 5, 8])
set3 = set1 ^ set2
print(set3)
# {1, 3, 5, 8}
'''

# ПОДМНОЖЕСТВА и НАДМНОЖЕСТВА
# ( метод:  issubset())
# ИЛИ
# (оператор <= если: подмножество <= надмножество (возвращает True, иначе False))
# (оперетор >= если: надмножество >= подмножество (возвращает True, иначе False))

# Предположим, что имеется два множества, и одно из этих множеств содержит
# все элементы другого множества. Вот пример:
'''
set1 = set([1, 2, 3, 4]) # надмножество
set2 = set([2, 3])       # подмножество
print(set1.issubset(set2))
# False
'''
'''
set1 = set([1, 2, 3, 4])
set2 = set([2, 3])
print(set2.issubset(set1))
# True
'''
# В этом примере setl содержит все элементы set2. Это означает, что set2 является
# подмно­жеством setl. Это также означает, что setl является надмножеством set2.

# множество2.issuЬsеt(множество1)

# Данный метод возвращает True, если множество2 является подмножеством множестваl.
# В противном случае он возвращает False.


# Программа 9.3
# В этой рубрике вы рассмотрите программу 9.3, которая демонстрирует различные операции
# над множествами. Данная программа создает два множества: одно содержит имена студен­тов
# из бейсбольной команды, другое - имена студентов из баскетбольной команды. Затем
# программа выполняет приведенные ниже операции:

# + находит пересечение множеств, чтобы показать имена студентов, которые играют в
# обеих спортивных командах;

# + находит объединение множеств, чтобы показать имена студентов, которые играют в
# лю­бой команде;

# + находит разность бейсбольного и баскетбольного множеств (бейсбол -баскетбол), чтобы
# показать имена студентов, которые играют в бейсбол, но не играют в баскетбол;

# + находит разность баскетбольного и бейсбольного множеств (баскетбол - бейсбол), чтобы
# показать имена студентов, которые играют в баскетбол, но не играют в бейсбол;

# + находит симметричную разность баскетбольного и бейсбольного множеств, чтобы пока­зать
# имена студентов, которые занимаются одним из этих видов спорта, но не обоими одновременно.
'''
baseball = set(['Dgody', 'Karmen', 'Aida', 'Alisia'])
basketball = set(['Eva', 'Karmen', 'Alisia', 'Sara'])

# Напечатаем имена студентов которые занимаются бейсболом:

print('B бейсбольной команде играют: ')
for names in baseball:
    print(names)

print('B баскетбольной команде играют: ')
for names in basketball:
    print(names)

# Пересечение
print('Они играют и в бейсбол и в баскетбол: ')
for names in baseball & basketball:
    print(names)

# Объединение
print('Bce они спортсмены: ')
for names in baseball.union(basketball):
    print(names)

# Разность
print('Они играют в бейсбол но не в баскет: ')
for names in baseball - basketball:
    print(names)

print('Они играют в баскет но не бейсбол: ')
for names in basketball - baseball:
    print(names)

# Симетричная разность
print('Они занимаются только одним видом спорта: ')
for names in baseball ^ basketball:
    print(names)
'''

# Включение в множество

# Включение в множество - это выражение, которое читает последовательность
# входных элементов и использует эти элементы для создания множества.

# Включение в мно­жество работает так же, как включение в список, и записывается
# аналогично, как и включение в список. Отличие состоит в том, что включение в
# множе­ство использует фигурные скобки ({ }), а включение в список - квадратные скобки ([]).

# Предположим, у нас есть следующее множество:
'''
setl = set([1, 2 , 3, 4, 5 ])
'''
# Создадим копию этого множества, применяя метод "включение в множество":
'''
set2 = {item for item in setl}
print(set2)
# {1, 2, 3, 4, 5}
'''
# Давайте рассмотрим еще один пример. Приведенный ниже фрагмент кода создает множество чисел, а затем создает второе множество, содержащее квадраты всех чисел из первого множества:
'''
set2 = {item**2 for item in setl}
print(set2)
# {1, 4, 9, 16, 25}
'''
# С включением в множество также можно использовать условие if. Например, предположим, что множество содержит целые числа, и вы хотите создать второе множество, содержащее только целые числа из первого множества, которые меньше 10.
'''
set1 = set([1, 20, 2, 30, 3, 50])
set2 = {item for item in set1 if item < 10}
print(set2)
# {1, 2, 3}
'''
'''
myset = set(25)
print(myset)
# Ошибка: данный элемент int (25) не итерируемый
'''
'''
myset = set('aaa bbb ggg')
print(myset)
# {'g', 'a', ' ', 'b'}
'''
'''
myset = set(['aaa', 'bbb', 'ggg'])
print(myset)
# {'aaa', 'bbb', 'ggg'}
'''

# СЕРИАЛИЗАЦИЯ объектов (пока не изучено)

# -------------------------------------------------------------------------------------------------

# Повторение мать учения
'''
dct = {'Mon':1, 'Tus':2, 'Wen':3}
print(dct['Tus'])
# 2
'''
'''
dct = {'Mon':1, 'Tus':2, 'Wen':3}
print(dct.get('Mon', 'dont found'))
# 1
'''
'''
dct = {'Mon':1, 'Tus':2, 'Wen':3}
print(dct.get('Sun', 'dont found'))
# dont found
'''
'''
stuff = {'aaa': 111, '666': 222, 'ввв': 333}
print(len(stuff))
# 3
'''
'''
dct = {1:[0, 1], 2:[2, 3], 3:[4, 5]}
for k in dct:
    print(k)
# 1
# 2
# 3
'''
# ------------------------------------------------------------------------------------------

# Алгоритмический тренажер

# 1.
'''
dct = {'a': 1, 'b':2, 'c':3}
print(dct)
# {'a': 1, 'b': 2, 'c': 3}

# 2. Напишите инструкцию, которая создает пустой словарь.
dct = {}
print(dct)
# {}
'''
# 3. Предположим, что переменная dct ссылается на словарь. Напишите инструкцию if, ко­торая определяет, существует ли в словаре ключ 'Джеймс'. Если существует, покажите значение, которое связано с этим ключом. Если ключа в словаре нет, то покажите соот­ветствующее сообщение.
'''
dct = {'Джеймс':'555-1111', 'Кэти':'555-2222', 'Джоанна':'555-3333'}

if 'Джеймс' in dct:
    print(dct['Джеймс'])
else:
    print("'Джеймс' не найден")
'''
# 4. Предположим, что переменная dct ссылается на словарь. Напишите инструкцию if, которая определяет, существует ли в словаре ключ 'Джеймс'. Если существует, удалите ключ 'Джим' и связанное с ним значение.
'''
dct = {'Джеймс':'555-1111', 'Кэти':'555-2222', 'Джоанна':'555-3333'}

if 'Джеймс' in dct:
    del dct['Джеймс']
    print(dct)
else:
    print("'Джеймс' не найден")
'''
# 5. Напишите фрагмент кода, который создает множество с приведенными далее целыми числами в качестве его членов: 1О, 20, 30 и 40.
'''
myset = set([10, 20, 30, 40])
print(myset)
# {40, 10, 20, 30}
'''
# 6. Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фрагмент кода, который создает еще одно множество, содержащее все элементы из setl и set2, и присваивает получившееся множество переменной set3.
'''
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set1.union(set2)
print(set3)
'''
# 7. Допустим, что обе переменные set1 и set2 ссылаются на множество. Напишите фраг­мент кода, который создает еще одно множество, содержащее только те элементы, кото­рые одновременно находятся в set1 и в set2, и присвойте получившееся множество переменной set3. (это пересечение)
'''
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set1 & set2
print(set3)
# {3, 4}
'''
# 8. Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фраг­мент кода, который создает еще одно множество, содержащее все элементы setl, не входящие в set2, и присвойте получившееся множество переменной set3.
'''
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set1 - set2
print(set3)
# {1, 2}
'''
# 9. Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фраг­мент кода, который создает еще одно множество, содержащее все элементы set2, не входящие в setl, и присвойте получившееся множество переменной set3.
'''
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set2 - set1
print(set3)
# {5, 6}
'''
# 1О. Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фраг­мент кода, который создает еще одно множество с элементами, не принадлежащими одновременно setl и set2, и присвойте получившееся множество переменной set3.
'''
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set2 ^ set1
print(set3)
# {1, 2, 5, 6}
'''
# 11. Предположим, что существует следующий список: numbers = [1, 2, 3, 4, 5]. Напишите инструкцию, в которой используется включение в словарь для создания сло­варя, в котором каждый элемент содержит число из списка numbers в качестве ключа и произведение этого числа на 1О в качестве значения. Другими словами, словарь должен содержать следующие элементы: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
'''
numbers = [1, 2, 3, 4, 5]
result = {num:num*10 for num in numbers}
print(result)
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
'''
'''
numbers = [1, 2, 3, 4, 5]
dct = {}
dct = {k:k*10 for k in numbers}
print(dct)
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
'''
# 12. существует следующий словарь:
'''
test_averages = { 'Dganel': 98, 'Sem': 87, 'Dgenifer': 92, 
                 'Tomas': 74, 'Sally': 89, 'Zeb' : 84}
# Напишите инструкцию, в которой используется включение в словарь для создания вто­рого словаря с именем high_scores. Словарь high_scores должен содержать все элемен­ты словаря test_averages, в котором значение равно 90 или больше.

high_scores = {}
for k, v in test_averages.items():
    if v >= 90:
        high_scores[k] = v
print(high_scores)
# {'Dganel': 98, 'Dgenifer': 92}
'''
# -------------------------------------------------------------------------------------------

# Упражнения по программированию: (Глава 9. Словари и множества стр.524)

# 1. Программа должна позволить пользователю ввести номер курса, а затем показать номер аудитории, имя преподавателя и время проведения курса.
'''
# номера курсов и номера аудиторий, где проводятся курсы.
course_audience = {'CS101':3004, 'CS102':4501, 
                   'CS103':6755, 'CS104':1244, 
                   'CS105':1411}
# номера курсов и имена препо­давателей, которые ведут каждый курс.
course_teachers = {'CS101':'Hains', 'CS102':'Alvarado', 
                   'CS103':'Rich', 'CS104':'Berk', 
                   'CS105':'Lee'}
# номера курсов и время проведе­ния каждого курса.
course_times = {'CS101':'8:00', 'CS102':'9:00', 
                   'CS103':'10:00', 'CS104':'11:00', 
                   'CS105':'13:00'}

my_key = input('Enter number of course: ')

print(f' Ввша аудитория: {course_audience[my_key]} \n преподаватель: {course_teachers[my_key]} \n время проведения в: {course_times[my_key]}')
'''

# 2. Викторина со столицами.
# Напишите программу, которая создает словарь, содержащий в качестве ключей названия шести стран и в качестве значений - их столицы. Затем про­грамма должна провести викторину, случайным образом выводя название страны и пред­лагая ввести его столицу. Программа должна провести подсчет количества правильных и неправильных ответов.
'''
import random
country_capital = {'USA': 'Vashington', 'Cuba': 'Havana', 
                   'Japan': 'Tokyo', 'Italy': 'Rome',
                   'France': 'Paris', 'Iran': 'Tehran'}

# Переменные для подсчета правильных и неправильных ответов
correct_answers = 0
incorrect_answers = 0

# Количество вопросов в викторине
questions_count = 5

for _ in range(questions_count):
    random_country = random.choice(list(country_capital.keys()))
    capital_resp = input(f'Какова столица {random_country}? ')

    # Проверка ответа
    if capital_resp.strip() == country_capital[random_country]:
        print('Верно!')
        correct_answers += 1
    else:
        print(f'Неверно! Правильный ответ: {country_capital[random_country]}')
        incorrect_answers += 1

# Подсчет и вывод результатов
print("\nBиктopинa окончена!")
print(f"Правильных ответов: {correct_answers}")
print(f"Неправильных ответов: {incorrect_answers}")
'''

# Как работает программа:
# Создание словаря: В начале создается словарь country_capital, где ключами являются названия стран, а значениями — их столицы.
# Переменные для подсчета: Инициализируются счетчики для правильных и неправильных ответов.
# Цикл викторины: Программа задает пользователю вопросы. Она выбирает случайную страну и предлагает ввести ее столицу.
# Проверка ответа: Ввод пользователя сравнивается с правильным ответом. При правильном ответе увеличивается счетчик правильных ответов. При неправильном — счетчик неправильных ответов, и выводится правильный ответ.
# Вывод результатов: По окончании викторины выводится количество правильных и неправильных ответов.
