# Функции

# бывают без возврата значения и с возвратом значения.
# Для того чтобы создать функцию, пишут ее определение. Вот общий формат определения
# функции в Python:

# def имя_функции():
# инструкция
# инструкция

# pass - это ключевое слово (используют для создания пустых ф-ий).
#  можно использовать в качестве местозаполнителя в любом месте
# про­граммного кода Pythoп.
# Например, его можно использовать в инструкции if, как показано ниже:

# if х > у:
#   pass
# else:
#   pass

# Локальные переменные:

# Локальная переменная создается внутри функции. Инструкции, которые находятся за
# пределами функции, к ней доступа не имеют. Разные функции могут иметь локальные
# переменные с одинаковыми именами, потому что функции не видят локальных перемен­-
# ных друг друга.

# К локальной переменной НЕ может обращаться программный код, который появляется
# внутри функции в точке до того, как переменная бьта создана.

# Передача аргументов в функцию:

# Аргумент -
# это любая порция данных, которая передается в функцию, когда функция вызывается .
# Параметр -
# это переменная, которая получает аргумент, переданныйв функцию .

# Пара­метрическая переменная, часто именуемая просто параметром, - это специальная
# пере­менная, которой присваивается значение аргумента, когда функция вызывается.

# Например: Эта программа демонстрирует аргумент, передаваемый в функцию.
'''
def main():
    value = 5
    show_double(value)

def show_double(number):
    result = number * 2
    print(result)

main()
'''
# Следующая програм­ма 5.8 содержит функцию show_sum, которая принимает два аргумента,
# (num1 u num2 вводит пользователь)складывает их и по­казывает сумму.
'''
def main():
    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))
    show_sum(num1, num2)
    
def show_sum(num1, num2):
    result = num1 + num2
    print(result)

main()
'''
# Внесение изменений в параметры:
# Когда аргумент передается в функцию Python, параметрическая переменная функции
# будет ссылаться на значение этого аргумента. Однако любые изменения,
# которые вносятся в параметрическую переменную, не будут влиять на аргумент.
# Для того чтобы это продемонстрировать, взгляните на программу:
'''
def main():
    value = 99
    print(value)
    change_me(value)
    print(value) # 'После возвращения в функцию main значение равно 99
    
def change_me(arg):
    arg = 0
    print(arg) 

main()
# Будет выведено:
# 99
# 0
# 99
'''
# Именованные аргументы:

#  Python позволяет писать аргумент в приведенном ниже формате, чтобы
# указывать, какой параметрической переменной аргумент должен быть передан:

# имя_параметра = значение

# В таком формате имя_параметра - это имя параметрической переменной,
# а значение - значение, передаваемое в этот параметр. Аргумент,
# написанный в соответствии с этой синтаксической конструкцией, называется
# ИМЕНОВАННЫМ АРГУМЕНТОМ.

# Поскольку имено­ванный аргумент определяет, в какой параметр этот аргумент должен быть передан,
# его позиция в вызове функции не имеет значения.

# В вызове функции имеется возможность смешивать позиционные и именованные аргумен­ты,
# но при этом позиционные аргументы должны стоять первыми, после которых идут име­нованные аргументы.

#  Вот пример того, как можно было бы вызвать функцию show_interest в программе 5.10 с помощью
# позиционных и именованных аргументов:

# show_interest(lOOOO.O, rate=0.01, periods=lO)

# ФУНКЦИЯ С ВОЗВРВТОМ ЗНАЧЕНИЯ -
# это функция, которая возвращает значение обратно в ту часть программы, которая ее вызвала.
#  Возвращаемое из функции значение используется как любое другое значение: оно может быть
# присвоено переменной, выведено на экран, ис­пользовано в математическом выражении
# (если оно является числом) и т. д.

# ФУНКЦИЯ БЕЗ ВОЗВРАТА ЗНАЧЕНИЯ - это группа инструкций, которая присутствует в программе
# с целью выполнения определенной задачи. Когда нужно , чтобы функция выполнила свою задачу,
# эта функция вызывается. В результате внутри функции исполняются инструкции.
# Когда функция завершается , поток управления программы возвращается к инструкции,
# которая располагается сразу после вызова функции.

# Генерирование случайных чисел

# Python предлагает несколько библиотечных функций для работы со случайными числами.
# Эти функции хранятся в модуле random в стандартной библиотеке. Для того чтобы применить
# любую из этих функций, сначала вверху программы нужно написать вот эту инструкцию импорта:

# import random

# Первая функция генерации случайного числа, которую мы обсудим, называется randint.
# Функции randint возвращают целое число.
# Вот пример вызова функции randint:  (аргументы в скобках показывают диапазон включая 1 и 100)

# number = random.randint(l, 100)

# Вызов функций из f-строки:
# Вызов функции можно использовать в качестве местозаполнителя в f-строке. Вот пример:

# print(f'Чиcлo равняется {random.randint(l, 100):>10d}')
# Например:
'''
import random
num = random.randint(1, 10)
print(num)
# вывелось в данном случае 6
'''
#  Написать симулятор десяти кратного поочередного подбрасывания монеты .
# Всякий раз, когда программа имитирует подбрасывание монеты, она должна
# случайным образом показывать "орла" или "решку".
# Буду пиcть инструкцию if, которая показывает "орла", если
# слу­чайное число равняется 1, или "решку" в противном случае.
'''
import random

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for i in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орел')
        else:
            print('Решка')
main()
'''

# Функции randrange, random и uniform

# Функция randrange  возвращает случайно отобранное значениеиз последовательности значений.
# Функции randint и randrange возвращают целое число.
# Например, приведенная ниже инструкция присваивает переменной numЬer случайное число
# в диапазоне от О до 9:

# nunber = random.randrange(lO)

# Функция возвратит случайно отобранное число из последовательности значений от О до
# конечного предела, но исключая сам предел.

# Приведенная ниже инструкция задает начальное значение,конечный предел и величину шага:

# nwnЬer = random.randrange(O, 101, 10)

#  функция random возвращает случайное число с плавающей точкой. В функцию random никаких
# аргументов не передается. Во время ее вызова она возвращает случайное число с плавающей
# точкой в диапазоне от О.О до 1.0 (но исключая 1.0). Вот пример:

# numЬer = random.random()

# Функция uniform тоже возвращает случайное число с плавающей точкой, но при этом она
# позволяет задавать диапазон значений, из которого следует отбирать значения.
# Вот пример:

# numЬer = random.uniform(l.O, 10.0)

# В этой инструкции функция uniform возвращает случайное число с плавающей точкой
# в диапазоне от 1.0 до 1О.О и присваивает его переменной numЬer.

# Функция с возвратом значения
# имеет инструкцию
# return
# которая возвращает значение в ту часть программы, которая ее вызвала.

# Oбщий формат определения функции с возвратом значения:

# def имя_функции():
#   инструкция
#   инструкция
#   return выражение

# Математический модуль math

# Математический модуль math стандартной библиотеки Python содержит многочисленные
# функции для использования в математических расчетах.

# инструкцию import math следует писать в любой программе, которая исполь­зует модуль math.

# Математический модуль math также определяет две переменные, pi и е, которым присвоены
# математические значения констант pi (3.14159265) и е (2.71828). Эти переменные можно
# применять в уравнениях, которые требуют их значений. Например, приведенная ниже
# инструкция, вычисляющая площадь круга, использует pi. (Обратите внимание,
# что для обращения к данной переменной применяется форма записи через точку).

# area = math.pi * radius**2  (это пи эр квадрат)
