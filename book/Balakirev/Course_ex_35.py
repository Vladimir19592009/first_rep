# 35. Функции: первое знакомство, определение def и их вызов.
# (https://www.youtube.com/watch?v=NUrEyTW4JuU&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# В Python существует множество стандартных, встроенных функций, но на все случаи жизни их не придумаешь. Поэтому, программист может сам создавать свои собственные по мере необходимости. Для этого используется следующий синтаксис:

# def <имя функции>([список аргументов]):
#         оператор 1
#         оператор 2
#         …
#         оператор N

#  имя функции придумывается программистом подобно именам переменных и, так как функция – это определенное действие, то ее имя следует выбирать как глагол, например:

# go, show, get, set и т.п.

# Далее, идет набор операторов, которые образуют тело функции. Именно они начинают выполнятся при ее вызове.
# Давайте в качестве примера, зададим простую функцию, которая будет имитировать отправку письма:

# def send_mail():
#     text = "Уважаемый, Сергей Балакирев! Я так и не понял, что такое функция. Объясните лучше!"
#     print(text)


# send_mail()

# обратите внимание, мы можем вызывать функцию только после ее объявления. То есть, сначала сделать ее вызов, а потом объявить не получится, возникнет ошибка, что имя send_mail не определено. Нужно сначала объявлять функции и только потом их вызывать.
# Сейчас у нашей функции нет никаких параметров. Давайте добавим один с именем отправителя:

# def send_mail(from_name):
#     text = f"""Уважаемый, Сергей Балакирев!
# Я так и не понял, что такое функция.
# Объясните лучше!
# Ваш, навсегда {from_name}!"""
#     print(text)


# send_mail("Иван Иванович")

# Для этого в круглых скобках записываем параметр с именем from_name и, затем, в многострочной F-строке мы добавим это имя в конце сообщения.
# функции нужно передавать ровно столько аргументов, сколько параметров в ней определено. Давайте пропишем второй параметр – возраст отправителя:

# def send_mail(from_name, old):
#     text = f"""Уважаемый, Сергей Балакирев!
# Я так и не понял, что такое функция.
# Объясните лучше!
# Ваш, навсегда {from_name}! И не судите строго, мне всего {old} лет."""

#     print(text)


# send_mail("Иван Иванович", 7)


# 36. Оператор return в функциях. Функциональное программирование
# (https://www.youtube.com/watch?v=D2uB3vqMTzI&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# давайте объявим функцию, которая бы вычисляла квадратный корень из положительных чисел:

# def get_sqrt(x):
#     res = None if x < 0 else x ** 0.5
#     return res

# переменная res будет принимать None для отрицательных значений и квадратный корень – для неотрицательных.
# a = get_sqrt(49)
# print(a)  # 7.0


# Давайте зададим в программе еще одну функцию для определения максимального значения среди двух чисел:

# def get_max2(a, b):
#     return a if a > b else b


# x, y = 5, 7
# print(get_max2(x, y))
# 7

# Давайте теперь усложним задачу и будем искать максимум среди трех чисел. Определим три переменные и воспользуемся все той же функцией get_max2():

# x, y, z = 5, 7, 10
# print(get_max2(x,get_max2(y, z)))
# 10
# Сначала будет вызвана функция, записанная в качестве аргумента, которая возвратит максимальное среди чисел 7 и 10, то есть, значение 10, а затем, вызывается первая функция, которая определяет максимум из чисел 5 и 10. Соответственно, на выходе получаем результат 10, который и выводится в консоль.


# 37. Алгоритм Евклида для нахождения НОД (наибольший общий делитель)
# (https://www.youtube.com/watch?v=IEORD_eVfCo&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# вначале пару слов о самом алгоритме Евклида, о принципе его работы. Сначала рассмотрим его медленный, но простой вариант.

# Например, пусть даны два натуральных числа: a = 18 и b = 24. Чтобы определить для них НОД, будем действовать, следующим образом. Из большего значения вычтем меньшее и результат сохраним в переменной с большим значением, то есть, в b. Фактически, это означает, что мы выполняем операцию: b = b - a. Теперь у нас два значения a = 18, b = 6. Для них повторяем тот же самый процесс. Здесь большее уже переменная a, поэтому, корректируем ее значение, вычитая меньшее. Получаем новую пару a = 12, b = 6. Опять повторяем этот процесс и видим, что a = 6, b = 6 – переменные равны. В этом случае останавливаем алгоритм и получаем, что НОД(18, 24) = 6, что, в общем то, верно.

# Весь этот алгоритм можно представить следующим псевдокодом:

# пока a != b
#          находим большее среди a и b
#          уменьшаем большее на величину меньшего

# выводим полученное значение величины a (или b)

# Давайте его опишем с помощью, следующей функции:

# def get_nod(a, b):
#     """Вычисляется НОД для натуральных чисел a и b
#         по алгоритму Евклида.
#         Возвращает вычисленный НОД.
#     """
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a

#     return a


# print(get_nod(18, 24))
# 6

# После того, как функция определена, ее следует протестировать и убедиться в корректности возвращаемых результатов. Для этого тестировщик создает свою вспомогательную функцию. Используя наши текущие знания, мы ее опишем, следующим образом:

# import time

# def test_nod(func):
# -- тест №1 -------------------------------
# a = 28
# b = 35
# res = func(a, b)
# if res == 7:
#     print("#test1 - ok")
# else:
#     print("#test1 - fail")

# -- тест №2 -------------------------------
# a = 100
# b = 1
# res = func(a, b)
# if res == 1:
#     print("#test2 - ok")
# else:
#     print("#test2 - fail")

# # -- тест №3 -------------------------------
# a = 2
# b = 100000000

# st = time.time()
# res = func(a, b)
# et = time.time()
# dt = et - st
# if res == 2 and dt < 1:
#     print("#test3 - ok")
# else:
#     print("#test3 - fail")

# test_nod(get_nod)
# test1 - ok
# test2 - ok
# test3 - fail


# Смотрите, если взять два числа a = 2 и b = 100, то по изначальному алгоритму мы будем делать многочисленные вычитания из b a, пока значения не сравняются. То есть, мы здесь, фактически, вычисляем остаток от вхождения двойки в сотню, а это есть не что иное, как операция:

# b = b % a = 0

# И никаких циклических вычитаний! Это, очевидно, будет работать много быстрее. При этом, как только получаем остаток равный нулю, то НОД – это значение меньшей переменной, то есть, в нашем примере – a = 2.

# То же самое для предыдущих значений a = 18, b = 24. Получаем серию таких вычислений:

# b = 24 % 18 = 6
# a = 18 % 6 = 0

# Значит, НОД(18, 24) = 6. Видите, как это быстро и просто! На уровне псевдокода быстрый алгоритм Евклида можно описать так:

# пока меньшее число больше 0
#  большему числу присваиваем остаток от деления на меньшее число
# выводим большее число

# Реализуем его в виде функции:

# def get_fast_nod(a, b):
#     """Вычисляется НОД для натуральных чисел a и b
#         по быстрому алгоритму Евклида.
#         Возвращает вычисленный НОД.
#     """
#     if a < b:
#         a, b = b, a

#     while b != 0:
#         a, b = b, a % b

#     return a


# test_nod(get_fast_nod)
# test1 - ok
# test2 - ok
# test3 - ok


# 38. Именованные аргументы. Фактические и формальные параметры
# (https://www.youtube.com/watch?v=8Z-_PpJbkdI&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# Например, простая функция вычисления объема прямоугольного параллелепипеда, очевидно должна принимать, как минимум, три параметра (ширину, высоту и глубину):

# def get_V(a, b, c):
#     print(f"a = {a}, b = {b}, c = {c}")
#     return a * b * c


# v = get_V(1, 2, 3)
# print(v)
# a = 1, b = 2, c = 3
# 6

# здесь используется позиционная запись аргументов при вызове функции, то есть, значения параметров a, b, c определяются порядком записи аргументов. А можно ли, не меняя порядка, параметру b присвоить 1, параметру c – 2, а a – 3? Оказывается да, в языке Python такое возможно, если явно указывать имена параметров при вызове функции:

# v = get_V(b=1, a=2, c=3)
# print(v)
# a = 2, b = 1, c = 3
# 6

# Такие аргументы называются именованными. Теперь, при запуске программы, мы видим, указанные значения у параметров a, b и c.
# А можем ли мы комбинировать позиционные и именованные аргументы? Да и такое тоже возможно. Только вначале следует указывать позиционные, а в конце – именованные, например, так:

# v = get_V(1, c=2, b=3)
# print(v)
# a = 1, b = 3, c = 2
# 6

# v = get_V(1, 2, c=3)
# print(v)
# a = 1, b = 2, c = 3
# 6

# Причем, обратите внимание, последним именованным аргументом здесь может быть только имя параметра c.

# --------------------------------------------------


# Вернемся теперь к параметрам самой функции. Мы их объявили просто через запятую с именами a, b, c. Однако, можно задавать параметры со значениями по умолчанию, например, так:

# def get_V(a, b, c, verbose=True):
#     if verbose:
#         print(f"a = {a}, b = {b}, c = {c}")

# return a * b * c
# Такие параметры называются формальными, а обычные – фактическими. В чем отличие формальных параметров от фактических, помимо значений по умолчанию? Их не обязательно прописывать при вызове функции. Например, наш прежний вызов:
# v = get_V(1, 2, 3)
# print(v)
# a = 1, b = 2, c = 3
# 6

# сработает без каких-либо проблем. Мы не указали аргумент для последнего формального параметра verbose. В этом случае он принимает значение по умолчанию True. Если же указать его:

# v = get_V(1, 2, 3, False)
# print(v)
# 6
# то функция print() внутри функции вызвана уже не будет. Разумеется, можно использовать и соответствующий именованный аргумент:

# v = get_V(1, 2, 3, verbose=False)  # Все будет работать также.
# print(v)
# 6

# Зачем вообще нужны формальные параметры и когда их следует использовать? Я, думаю, ответ здесь очевиден – для удобства использования функций. Как мы только что видели, аргументы формальным параметрам можно не передавать, если нас устраивает поведение функции по умолчанию. В других, как полагается, редких ситуациях, всегда можно поменять значение такого параметра на другое и скорректировать работу функции.


# 39. Функции с произвольным числом параметров *args и **kwargs
# (https://www.youtube.com/watch?v=6Kk7luuKPGQ&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# На этом занятии узнаем, как функциям можно передавать произвольное число аргументов. Где это используется, я думаю, вы понимаете? Например, известная нам функция

# print(max(1, 2, 3, -4))
# 3
# может принимать разное число аргументов и возвращает максимальное значение. Как можно самим определять такие функции? Делается это очень просто. Допустим, мы с вами хотим задать функцию для формирования маршрута к файлу: ( F:\~stepik.org\Добрый, добрый Python (Питон)\39\p39. Функции.docx )

# Опишем такую функцию. Я назову ее os_path(), а вместо списка параметров запишу звездочку и одну переменную args:

# def os_path(*args):
#     print(args)

# Для начала, посмотрим, как это будет работать. Вызовем функцию с тремя строковыми аргументами:
# os_path("F:\\~stepik.org", "Добрый, добрый Python (Питон)", "39\\p39. Функции.docx")
# ('F:\\~stepik.org', 'Добрый, добрый Python (Питон)', '39\\p39. Функции.docx')

# Не забываем здесь про экранирование обратных слешей. Выполним эту программу и в консоли видим, что переменная args ссылается на кортеж со значениями переданных трех аргументов. Чтобы функция принимала произвольное число аргументов, в ее объявлении достаточно у параметра прописать оператор *. Это оператор упаковки аргументов в кортеж и через переменную args мы сможем с ним работать.

# Давайте теперь довершим нашу функцию и сформируем полный путь на основе его фрагментов. Сделать это можно с помощью знакомого нам метода join(), следующим образом:

# def os_path(*args):
#     path = "\\".join(args)
#     return path


# p = os_path("F:\\~stepik.org", "Добрый, добрый Python (Питон)", "39\\p39. Функции.docx")
# print(p)
# F:\~stepik.org\Добрый, добрый Python (Питон)\39\p39. Функции.docx

# Хорошо, а что если мы передадим этой функции дополнительно один именованный аргумент:

# p = os_path("F:\\~stepik.org",
#             "Добрый, добрый Python (Питон)",
#             "39\\p39. Функции.docx",
#             sep='/'  # именованный аргумент
# )
# TypeError: os_path() got an unexpected keyword argument 'sep'

# При запуске программы увидим ошибку, что функция не имеет такого формального параметра. Дело в том, что записывая объявление *args мы определяем лишь произвольное число фактических параметров, но не формальных. Как это можно поправить? Здесь есть, по крайней мере, два способа. В самом простом варианте, достаточно прописать этот формальный параметр в объявлении функции:
# def os_path(*args, sep='\\'):
#     path = sep.join(args)
#     return path
# И теперь никаких проблем с вызовом нет. Но, конечно, указать, какой-либо другой именованный аргумент мы не можем:

# p = os_path("F:\\~stepik.org",
#             "Добрый, добрый Python (Питон)",
#             "39\\p39. Функции.docx",
#             sep='/', trim=True
# )
# TypeError: os_path() got an unexpected keyword argument 'sep'

# Снова получим ту же самую ошибку. Так как же определить в функции произвольное число формальных параметров? Делается это с помощью следующего синтаксиса:

# def os_path(*args, **kwargs):
#     print(kwargs)
#     path = kwargs['sep'].join(args)
#     return path

# Мы прописываем уже две звездочки, а затем, имя переменной, которая будет ссылаться на упакованные значения в виде словаря. Убедимся в этом, выполним программу и смотрите, в консоли коллекция kwargs действительно представляет собой словарь, ключами которого являются имена аргументов, а значениями – значения аргументов. Все очень удобно и просто, как всегда в Python!
# Причем, коллекция **kwargs обязательно должна быть записана после коллекции *args, наоборот нельзя, так как вначале должны идти фактические параметры и только потом – формальные. Мало того, мы можем некоторые параметры указывать явно, например:

# def os_path(*args, sep='\\', **kwargs):
#     path = sep.join(args)
#     return path

# И, тем самым, гарантировать их существование внутри функции. А другие, передаваемые именованные аргументы, следует проверять, прежде чем использовать, например, для параметра trim сначала делаем проверку его существования в словаре kwargs, а затем, смотрим, чему равно это значение:

# def os_path(*args, sep='\\', **kwargs):
#     if 'trim' in kwargs and kwargs['trim']:
#         args = [x.strip() for x in args]

#     path = sep.join(args)
#     return path
# Если условие выполняется, то удаляем пробелы до и после фрагментов путей к файлу.

# То же самое и с фактическими параметрами. Некоторые из них можно явно указать, при объявлении функции:

# def os_path(disk, *args, sep='\\', **kwargs):
#     args = (disk,) + args

#     if 'trim' in kwargs and kwargs['trim']:
#         args = [x.strip() for x in args]

#     path = sep.join(args)
#     return path
# И тогда на первый аргумент будет ссылаться параметр disk, а остальные позиционные аргументы упаковываться в коллекцию args:

# p = os_path("F:", "~stepik.org",
#             "Добрый, добрый Python (Питон)",
#             "39\\p39. Функции.docx",
#             sep='/', trim=True
# )
# Вот принцип, по которому объявляются функции с произвольным числом фактических и формальных параметров.


# 40. Операторы * и ** для упаковки и распаковки коллекций
# (https://www.youtube.com/watch?v=D6-d5yWOBd0&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# На этом занятии я хочу немного отступить от темы функций и рассказать об операторах * и **. Мы знаем, что они позволяют упаковывать аргументы в кортеж и словарь. Но их можно использовать не только в объявлении функций, но и при работе с разными коллекциями. Например, если взять кортеж из двух значений:

# x, y = (1, 2)
# print(x)  # 1
# print(y)  # 2

# то его можно распаковать в две переменные. Но, если мы пропишем там больше значений, например, четыре: то получим ошибку так как элементов четыре, а переменных всего две. Но, используя оператор *, мы можем упаковать оставшиеся значения во вторую переменную: (или наоборот в первую).

# x, *y = (1, 2, 3, 4)
# print(x)  # 1
# print(y)  # [2, 3, 4]

# *x, y = (1, 2, 3, 4)
# print(x)  # [1, 2,  3]
# print(y)  # 4

# То же самое можно проделывать и со списками:

# x, *y = [1, "a", True, 4]
# print(x)  # 1
# print(y)  # ['a', True, 4]

# и строками:

# *x, y, z = "Hello Python!"
# print(x)  # ['H', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o']
# print(y)  # n
# print(z)  # !

# И вообще с любыми итерируемыми объектами. То есть, оператор * упаковывает оставшиеся значения в список. Правда, мы не можем упаковывать уже упакованные данные, например, так:

# *y = 1, 2, 3
# произойдет ошибка, но вот так:

# x, *y = 1, 2, 3
# уже будет работать.

# Этот же оператор может выполнять и обратную операцию – распаковывать коллекции в набор данных. Пусть у нас имеется список:

# a = [1, 2, 3]
# print((a,))  # ([1, 2, 3],)

# то увидим кортеж со списком внутри. Но, если прописать оператор * перед списком:

# print((*a,))  # (1, 2, 3)

# то произойдет распаковка его элементов и список превратится в кортеж. То же самое можно сделать и при вызове функций. Допустим, определим кортеж из двух значений:

# d = -5, 5
# и вызовем с этими значениями функцию:

# range(d)
#     range(d)
#     ~~~~~^^^
# TypeError: 'tuple' object cannot be interpreted as an integer

# Возникнет ошибка, так как функция ожидает числа в качестве аргументов, а не коллекции. Но, мы можем распаковать кортеж d в два числа, поставив перед ним оператор *:

# print(range(*d))  # range(-5, 5)

# и теперь никаких ошибок нет. Давайте посмотрим, что вернет эта функция, преобразуем все к списку:

# print(list(range(*d)))
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
# Мы оператором * распаковали итерируемый объект и составили из его значений список.

# или

# print([*range(*d)])
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

# print(*range(*d))
# -5 -4 -3 -2 -1 0 1 2 3 4

# Мало того, мы таким образом можем делать объединение разных коллекций в одну коллекцию, например, список:
# a = [1, 2, 3]
# print([*range(*d), *(True, False), *a])
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, True, False, 1, 2, 3]

# Как видите, оператор * - невероятно удобный инструмент. И те же самые действия можно делать и со словарем. Зададим, следующий словарь с расшифровкой оценок:

# d = {0: "безнадежно", 1: "убого", 2: "неуд.", 3: "удовл.", 4: "хорошо", 5: "отлично"}
# Распаковать его можно двумя способами. Если прописать один оператор *:

# print({*d})  # {0, 1, 2, 3, 4, 5}
# получили множество, состоящее из ключей этого словаря. Или, можно сформировать список из ключей:

# print([*d])  # [0, 1, 2, 3, 4, 5]
# То есть, оператор * перебирает словарь как обычный итерируемый объект и по умолчанию, перебираются именно ключи. Если нам нужно перебрать значения, то следует вызвать дополнительно метод:

# print([*d.values()])  # ['безнадежно', 'убого', 'неуд.', 'удовл.', 'хорошо', 'отлично']
# получили список значений

# print([*d.items()])  # [(0, 'безнадежно'), (1, 'убого'), (2, 'неуд.'), (3, 'удовл.'), (4, 'хорошо'), (5, 'отлично')]
# получили список кортежей пар ключ значение

# Если же требуется распаковать словарь как словарь, то перед ним следует прописать две звездочки **:

# print({**d})  # {0: 'безнадежно', 1: 'убого', 2: 'неуд.', 3: 'удовл.', 4: 'хорошо', 5: 'отлично'}

# Теперь вместо множества мы получаем словарь. Где это нам может пригодиться? Например, для объединения нескольких словарей в один. Создадим еще один словарь:

# d2 = {6: "превосходно", 7: "элитарно", 8: "божественно"}

# И соединим их через распаковку данных:

# print({**d, **d2})
# {0: 'безнадежно', 1: 'убого', 2: 'неуд.', 3: 'удовл.', 4: 'хорошо', 5: 'отлично', 6: 'превосходно', 7: 'элитарно', 8: 'божественно'}

# На выходе получаем новый словарь с объединенными данными. Такой прием часто используется на практике, когда нужно объединить сразу несколько словарей

# А вот для упаковки оператор ** не используется.


# 41. Рекурсивные функции
# (https://www.youtube.com/watch?v=dtzoBXL11oo&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)


# 42. Анонимные (lambda) функции
# (https://www.youtube.com/watch?v=UAYeh7pSqXw&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# Лямбда функция определяется по очень простому синтаксису:

# lambda param_1, param_2, …: команда

# и записывается в программе, как оператор. Например, вот так можно определить лямбда-функцию для сложения двух значений:

# s = lambda a, b: a + b

# У нее два параметра a и b, а затем, через двоеточие написано, что с ними нужно сделать. Полученное значение будет автоматически возвращено этой функцией (никакого "return" не требуется). И, обратите внимание, у этой функции нет имени, поэтому она и называется анонимной. Но как тогда ее вызывать? Для этого объект-функцию, который создает лямбда-функция, нужно присвоить какой-либо переменной и через неё вызывать эту ф-ию:

# x = s(1, 2)
# print(s)  # <function <lambda> at 0x0000020133CC3C40>
# print(x)  # 3

# В чем особенность такого определения функции? Зачем ее придумали и почему бы не пользоваться обычными функциями? У нее есть одно принципиальное отличие от ранее рассматриваемых нами функций – она может быть записана как элемент любой конструкции языка Python. Например, прямо как элемент списка:

# a = [4, 5, lambda a, b: a + b, 7, 8]

# Мы здесь описываем лямбда-функцию и сразу же передаем ее в список. С обычными функциями так не получится. Они должны быть объявлены заранее и только потом мы могли бы передать ссылку на нее в список. Если мы сейчас обратимся к третьему элементу этого списка, запустим его прописав круглые скобки:

# print(a[2])
#  <function <lambda> at 0x00000173B5833C40>  (ссылка на лямда ф-ию)
# x = a[2](10, 7)  # переменная "х" нужна для того чтобы фиксировать возвращаемое значение от lambda
# print(x)  # 17

# такой пример: Предположим, у нас имеется список:

# lst = [5, 3, 0, -6, 8, 10, 1]
# и мы хотим написать функцию, которая бы выбирала значения из этого списка по определенному критерию (фильтру):

# def get_filter(a, filter=None):
#     if filter is None:
#         return a

#     res = []
#     for x in a:
#         if filter(x):
#             res.append(x)

#     return res

# Здесь второй параметр filter – это ссылка на другую функцию, которая будет отбирать значения из списка lst. Если вызвать ее только с одним первым аргументом:
# r = get_filter(lst)
# print(r)  # [5, 3, 0, -6, 8, 10, 1]

# То увидим в консоли тот же самый список без изменений. Но, если вторым аргументом передать вот такую лямбда-функцию:
# r = get_filter(lst, lambda x: x % 2 == 0)
# print(r)  # [0, -6, 8, 10]

# то возвратится новый список, состоящий только из четных значений. Как это произошло? В этом примере второй параметр filter функции get_filter стал ссылаться на лямбда-функцию. Эта функция возвращает True для четных значений и False – для нечетных. Соответственно, в цикле при переборе элементов списка, условие будет срабатывать только для четных значений и только они будут добавляться в список res.

# Мало того, если нам понадобится быстро изменить фильтр, то достаточно поправить реализацию анонимной функции, например, для выделения только положительных чисел:

# r = get_filter(lst, lambda p: p > 0)
# print(r)  # [5, 3, 8, 10, 1]
# В этом одно из удобств этих анонимных функций – их можно сразу прописать в нужном месте программы.

# Однако, у таких функций есть одно существенное ограничение – в них можно прописать только одну конструкцию языка Python, то есть, выполнить только одну какую-либо команду. Также нельзя объявлять анонимные функции в несколько строк:
# lambda a:
#     print(a)

# вызовет синтаксическую ошибку. Наконец, в лямбда-функциях нельзя использовать оператор присваивания:
# lambda a: a = 1

# Это также вызовет синтаксическую ошибку. Здесь мы можем лишь создавать новый объект на основе входных параметров (или глобальных, общих переменных программы):

# s = lambda a: a + 1
# print(s(1))  # 2

# p = lambda: "hello python"
# print(p())  # hello python

# либо просто возвращать ссылки на уже существующие объекты:

# p = lambda a: a
# print(p)  # <function <lambda> at 0x000001B2545D9580>


# 43. Области видимости переменных. Ключевые слова global и nonlocal
# (https://www.youtube.com/watch?v=TacyWpUF1Kk&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# см. текстовую версию: (https://proproprogs.ru/python_base/python3-oblasti-vidimosti-peremennyh-klyuchevye-slova-global-i-nonlocal)


# #44. Замыкания в Python
# (https://www.youtube.com/watch?v=sJF7OMNgLUs&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# Как мы с вами видели на предыдущем занятии, функции можно объявлять внутри других функций. Например, так:

# def say_name(name):
#     def say_goodbye():
#         print("Don't say me goodbye, " + name + "!")

#     say_goodbye()

# say_name('Sergey')  # Don't say me goodbye, Sergey!

# Мы здесь сначала вызываем внешнюю функцию, затем, в ней формируется вложенная функция say_goodbye() и вызывается. В результате, в консоли видим сообщение «Don't say me goodbye, Sergey!».

# А теперь сделаем, следующее. Вместо вызова внутренней функции возвратим ссылку на нее с помощью оператора return:

# def say_name(name):
#     def say_goodbye():
#         print("Don't say me goodbye, " + name + "!")

#     return say_goodbye

# Конечно, после запуска программы мы не увидим никакого сообщения, так как внутренняя функция нигде не вызывается. Исправим это. Сохраним ссылку на функцию say_goodbye() в переменной f:

# f = say_name("Sergey")
# f()  # Don't say me goodbye, Sergey!

# откуда функция say_goodbye() берет значение переменной name? Ведь внешняя функция say_name() выполнилась и завершилась, а значит, все ее локальные переменные вроде как тоже должны были бы исчезнуть? Но нет, мы обращаемся к переменной name и успешно получаем ее значение! Почему? Давайте разберемся.

# Дело в том, что когда у нас имеется глобальная ссылка f на внутреннее, локальное окружение функции say_goodbye(), то это окружение продолжает существовать, оно не удаляется автоматически сборщиком мусора, именно из-за этой глобальной ссылки на него. А вместе с ним, продолжают существовать и все внешние локальные окружения, в данном случае – окружение функции say_name(), потому что также существует неявная, скрытая ссылка на него из внутреннего окружения. Такие ссылки формируются автоматически и позволяют, в частности, обращаться к переменным, объявленным в этих внешних окружениях. Именно поэтому функция print() в say_goodbye() имеет доступ к переменной name и эта переменная продолжает существовать, пока существует окружение say_goodbye, а значит и окружение say_name.

# Вот такой эффект, когда мы «держим» внутреннее локальное окружение и имеем возможность продолжать использовать переменные из внешних окружений, в программировании называется замыканием. Замыкание в том смысле, что мы держим внутреннее окружение say_goodbye переменной f из глобального окружения. Получается цепочка ссылок, замыкающаяся на глобальном окружении. Мало того, при каждом новом вызове внешней функции, формируется свое новое, независимое локальное окружение, со своими локальными переменными и соответствующими значениями:

# f = say_name("Sergey")
# f2 = say_name("Python")
# f()
# Don't say me goodbye, Sergey!
# f2()
# Don't say me goodbye, Python!


# Где может пригодиться такой функционал? Например, можно создать функцию-счетчик, которая бы увеличивала значение локальной переменной на единицу при каждом запуске:

# def counter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start

#     return step

# здесь используем ключевое слово nonlocal, чтобы переменная start изменялась во внешней локальной области, а не создавалась бы в текущей, локальной. Без этой строчки возникнет ошибка, из-за неопределенности: мы берем текущее значение start извне, а потом создавали бы переменную с тем же именем внутри области step. Так делать нельзя. И строчка nonlocal start четко указывает брать переменную start из внешней локальной области, а не создавать в текущей.

# Теперь можно сформировать несколько таких независимых счетчиков и выполнить их:

# c1 = counter(10)
# c2 = counter()
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())
# 11 1
# 12 2
# 13 3

# У нас, действительно, оба счетчика отработают независимо друг от друга.

# И приведу еще один пример с замыканиями. Предположим, мы хотим сделать функцию, которая бы удаляла ненужные символы в начале и конце строки. Через замыкание это можно реализовать, следующим образом:

# def strip_string(strip_chars=" "):
#     def do_strip(string):
#         return string.strip(strip_chars)

#     return do_strip

# Обратите внимание, вложенная функция тоже имеет параметр – строку, у которой будут удаляться ненужные символы. Далее, создадим два объекта с разным списком удаляемых символов:

# strip1 = strip_string()
# strip2 = strip_string(" !?,.;")

# print(strip1(" hello python!.. "))  # hello python!..
# print(strip2(" hello python!.. "))  # hello python

# первая функция strip1 убрала только пробелы, а вторая еще и восклицательный знак с точками. Таким образом, мы можем многократно использовать в программе функции strip1 и strip2, передавая им разные строки.


# 45. Введение в декораторы функций
# (https://www.youtube.com/watch?v=v0qZPplzwUQ&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd)

# import webbrowser

# Это декаратор:
# def validator(funk):
#     def wrapper(url):
#         print("Этот текст до выполнения ф-ии")
#         funk(url)
#         print("Этот текст после выполнения ф-ии")
#     return wrapper



# @validator                # это ссылка на декаратор
# Это декарируемая ф-ия:
# def open_url(url):
#     webbrowser.open(url)


# open_url('https://itproger.com')


# Спомощью декоратора мы имеем возможность осуществлять различные проверки перед выполнением основной ф-ии и сообщить результат в случае ошибки. 
# Например осуществим проверку наличия точки в url адресе (сначала уберём точку и выйдет только сообщение о некоректности вызова):

# def validator(funk):
#     def wrapper(url):
#         if '.' in url:
#             funk(url)
#         else:
#             print("Неверный url")
#     return wrapper


# @validator
# def open_url(url):
#     webbrowser.open(url)


# open_url('https://itprogercom')
# Неверный url


# вернём точку на место и результат будет: (сайт откроется:)
# def validator(funk):
#     def wrapper(url):
#         if '.' in url:
#             funk(url)
#         else:
#             print("Неверный url")
#     return wrapper


# @validator
# def open_url(url):
#     webbrowser.open(url)


# open_url('https://itproger.com')

# т.о декаратор позволяет какбы обернуть ф-ию в некую обёртку, которая обезопасит нашу основную ф-ию от предполагаемых ошибок. А если нам этого не нужно - можем просто убрать ссылу на декаратор и ф-ия будет срабатывать сразу...
# декараторов может быть сколько угодно, каждый из которых будет выполнять свою миссию...
