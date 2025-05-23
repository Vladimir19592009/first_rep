# ФУНКЦИИ

# Функции представляют блок кода, который выполняет определенную задачу и который можно повторно использовать в других частях программы. В предыдущих статьях уже использовались функции. В частности, функция print(), которая выводит некоторое значение на консоль. Python имеет множество встроенных функций и позволяет определять свои функции. Формальное определение функции:

# def имя_функции ([параметры]):
#     инструкции

# Определение функции начинается с выражения def, которое состоит из имени функции, набора скобок с параметрами и двоеточия. Параметры в скобках необязательны. А со следующей строки идет блок инструкций, которые выполняет функция. Все инструкции функции имеют отступы от начала строки.

# Например, определение простейшей функции:

# def say_hello():
#     print("Hello")

# Функция называется say_hello. Она не имеет параметров и содержит одну единственную инструкцию, которая выводит на консоль строку "Hello".

# Обратите внимание, что инструкции функции должны иметь отступы от начала функции. Например:

# def say_hello():
#     print("Hello")


# print("Bye")

# Здесь инструкция print("Bye") не имеет отступов от начала функции say_hello и поэтому в эту функцию не входит. Обычно между определением функции и остальными инструкциями, которые не входят в функцию, располагаются две пустых строки.

# Для вызова функции указывается имя функции, после которого в скобках идет передача значений для всех ее параметров:
# имя_функции ([параметры])

# Например, определим и вызовем функцию:

# def say_hello():    # определение функции say_hello
#     print("Hello")

# say_hello()          # вызов функции say_hello
# say_hello()
# say_hello()
# # Hello
# # Hello
# # Hello

# Обратите внимание, что функция сначала определяется, а потом вызывается.

# Если функция имеет одну инструкцию, то ее можно разместить на одной строке с остальным определением функции:

# def say_hello(): print("Hello")

# say_hello()

# Подобным образом можно определять и вызывать и другие функции. Например, определим и выполним несколько функций:

# def say_hello():
#     print("Hello")

# def say_goodbye():
#     print("Good Bye")

# say_hello()
# say_goodbye()
# # Hello
# # Good Bye


# ЛОКАЛЬНЫЕ ФУНКЦИИ

# Одни функции могут определяться внутри других функций - внутренние функции еще называют локальными. Локальные функции можно использовать только внутри той функции, в которой они определены. Например:

# def print_messages():
#     # определение локальных функций
#     def say_hello(): print("Hello")
#     def say_goodbye(): print("Good Bye")
#     # вызов локальных функций
#     say_hello()    # Hello
#     say_goodbye()  # Good Bye

# # Вызов функции print_messages
# print_messages()

# # say_hello() # вне функции print_messages функция say_hello не доступна

# Здесь функции say_hello() и say_goodbye() определены внутри функции print_messages() и поэтому по отношению к ней являются локальными. Соответственно они могут использоваться только внутри функции print_messages()

# ОРГАНИЗАЦИЯ ПРОГРАММЫ И ФУНКЦИЯ main()

# В программе может быть определено множество функций. И чтобы всех их упорядочить, одним из способов их организации является добавление специальной функции (обычно называется main), в которой потом уже вызываются другие функции:

# def main():
#     say_hello()
#     say_goodbye()

# def say_hello():
#     print("Hello")

# def say_goodbye():
#     print("Good Bye")

# # Вызов функции main
# main()
# # Hello
# # Good Bye


# ПАРАМЕТРЫ ФУНКЦИИ

# Функция может принимать параметры. Через параметры в функцию можно передавать данные. Банальный пример - функция print(), которая с помощью параметра принимает значение, выводимое на консоль.

# Теперь определим и используем свою функцию с параметрами:

# def say_hello(name):
#     print(f"Hello, {name}")

# say_hello("Tom")
# say_hello("Bob")
# say_hello("Alice")
# # Hello, Tom
# # Hello, Bob
# # Hello, Alice

# Функция say_hello имеет параметр name, и при вызове функции мы можем передать этому параметру какой-либо значение. Внутри функции мы можем использовать параметр как обычную переменную, например, вывести значение этого параметра на консоль функцией print.

# При вызове функции значения передаются параметрам по позиции. Например, определим и вызовем функцию с несколькими параметрами:

# def print_person(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")

# print_person("Tom", 37)
# # Name: Tom
# # Age: 37
# Первое значение - "Tom" передается первому параметру, то есть параметру name. Второе значение - 37 передается второму параметру - age.

# ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ

# Некоторые параметры функции мы можем сделать необязательными, указав для них значения по умолчанию при определении функции. Например:

# def say_hello(name="Tom"):
#     print(f"Hello, {name}")

# say_hello()          # здесь параметр name будет иметь значение "Tom"
# say_hello("Bob")     # здесь name = "Bob"
# # Hello, Tom
# # Hello, Bob

# Здесь параметр name является необязательным. И если мы не передаем при вызове функции для него значение, то применяется значение по умолчанию, то есть строка "Tom".

# Если функция имеет несколько параметров, то необязательные параметры должны идти после обязательных. Например:

# def print_person(name, age = 18):
#     print(f"Name: {name} Age: {age}")

# print_person("Bob")
# print_person("Tom", 37)
# # Name: Bob Age: 18
# # Name: Tom Age: 37

# Здесь параметр age является необязательным и по умолчанию имеет значение 18. Перед ним расположен обязательный параметр name. Поэтому при вызове функции мы можем не передавать значение параметру age, но параметру name передать значение необходимо.

# При необходимости мы можем сделать все параметры необязательными:

# def print_person(name = "Tom", age = 18):
#     print(f"Name: {name} Age: {age}")


# print_person()               # Name: Tom  Age: 18
# print_person("Bob")          # Name: Bob  Age: 18
# print_person("Sam", 37)      # Name: Sam  Age: 37

# Передача ЗНАЧЕНИЙ ПАРАМЕТРАМ по имени. Именованные параметры:

# В примерах выше при вызове функции значения передаются параметрами функции по позиции. Но также можно передавать значения параметрам по имени. Для этого при вызове функции указывается имя параметра и ему присваивается значение:

# def print_person(name, age):
#     print(f"Name: {name} Age: {age}")

# print_person(age = 22, name = "Tom")
# # Name: Tom Age: 22

# В данном случае значения параметрам age и name передаются по имени. И несмотря на то, что параметр name идет первым в определении функции, мы можем при вызове функции написать print_person(age = 22, name = "Tom") и таким образом передать число 22 параметру age, а строку "Tom" параметру name.

# Символ * позволяет установить, какие параметры будут именнованными - то есть такие параметры, которым можно передать значения только по имени. Все параметры, которые располагаются справа от символа *, получают значения только по имени:

# def print_person(name, *, age, company):
#     print(f"Name: {name} Age: {age} Company: {company}")

# print_person("Bob", age = 41, company ="Microsoft")    # Name: Bob  Age: 41  company: Microsoft

# В данном случае параметры age и company являются именнованными.

# Можно сделать все параметры именнованными, поставив перед списком параметров символ *:

# def print_person(*, name, age, company):
#     print(f"Name: {name} Age: {age} Company: {company}")
# print_person(age=25, name='Bob', company='IBM')
# # Name: Bob Age: 25 Company: IBM

# Если наоборот надо определить параметры, которым можно передавать значения только по позиции, то есть позиционные параметры, то можно использовать символ /: все параметры, которые идут до символа / , являются позиционными и могут получать значения только по позиции

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name} Age: {age} Company: {company}")


# print_person("Tom", company="JetBrains", age = 24)   # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)                              # Name: Bob  Age: 41  company: Microsoft

# В данном случае параметр name является позиционным.

# Для одной функции можно определять одновременно позиционные и именнованные параметры.

# def print_person(name, /, age = 18, *, company):
#     print(f"Name: {name} Age: {age} Company: {company}")

# print_person("Sam", company ="Google")               # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company ="JetBrains")        # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company ="Microsoft", age = 42)  # Name: Bob  Age: 42  company: Microsoft

# В данном случае параметр name располагается слева от символа /, поэтому является позиционным и обязательным - ему можно передать значение только по позиции.

# Параметр company является именнованным, так как располагается справа от символа *. Параметр age может получать значение по имени и по позиции.


# НЕОПРЕДЕЛЁННОЕ КОЛ-ВО ПАРАМЕТРОВ

# С помощью символа звездочки можно определить параметр, через который можно передавать неопределенное количество значений. Это может быть полезно, когда мы хотим, чтобы функция получала несколько значений, но мы точно не знаем, сколько именно. Например, определим функцию подсчета суммы чисел:

# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}")

# sum(1, 2, 3, 4, 5)   # sum = 15
# sum(3, 4, 5, 6)      # sum = 18

# В данном случае функция sum принимает один параметр - *numbers, но звездочка перед названием параметра указывает, что фактически на место этого параметра мы можем передать неопределенное количество значений или набор значений. В самой функции с помощью цикла for можно пройтись по этому набору, получить каждое значение из этого набора в переменную n и произвести с ним какие-нибудь действия. Например, в данном случае вычисляется сумма переданных чисел.


# ОПЕРАТОР return и ВОЗВРАЩЕНИЕ РЕЗУЛЬТАТА из функции

# Функция может возвращать результат. Для этого в функции используется оператор return, после которого указывается возвращаемое значение:

# def имя_функции ([параметры]):
#     инструкции
#     return возвращаемое_значение

# Определим простейшую функцию, которая возвращает значение:

# def get_message():
#     return "Hello METANIT.COM"

# Здесь после оператора return идет строка "Hello METANIT.COM" - это значение и будет возвращать функция get_message().

# Затем это результат функции можно присвоить переменной или использовать как обычное значение:

# def get_message():
#     return "Hello METANIT.COM"

# message = get_message()  # получаем результат функции get_message в переменную message
# print(message)           # Hello METANIT.COM

# # можно напрямую передать результат функции get_message
# print(get_message())     # Hello METANIT.COM

# После оператора return может идти и сложное вычислямое выражение, результат которого будет возвращаться из функции. Например, определим функцию, которая увеличивает число в два раза:

# def double(number):
#     return 2 * number

# result1 = double(4)  # result1 = 8
# result2 = double(5)  # result2 = 10
# print(f"result1 = {result1}")   # result1 = 8
# print(f"result2 = {result2}")   # result2 = 10

# Или другой пример - получение суммы чисел:

# def sum(a, b):
#     return a + b

# result = sum(4, 6)                   # result = 0
# print(f"sum(4, 6) = {result}")       # sum(4, 6) = 10
# print(f"sum(3, 5) = {sum(3, 5)}")    # sum(3, 5) = 8

# ВЫХОД ИЗ ФУНКЦИИ

# Оператор return не только возвращает значение, но и производит выход из функции. Поэтому он должен определяться после остальных инструкций. Например:

# def get_message():
#     return "Hello METANIT.COM"
#     print("End of the function")

# print(get_message())
# # Hello METANIT.COM

# С точки зрения синтаксиса данная функция корректна, однако ее инструкция print("End of the function") не имеет смысла - она никогда не выполнится, так как до ее выполнения оператор return возвратит значение и произведет выход из функции.

# Однако мы можем использовать оператор return и в таких функциях, которые не возвращают никакого значения. В этом случае после оператора return не ставится никакого возвращаемого значения. Типичная ситуация - в зависимости от опеределенных условий произвести выход из функции:

# def print_person(name, age):
#     if age > 120 or age < 1:
#         print("Invalid age")
#         return
#     print(f"Name: {name} Age: {age}")

# print_person("Tom", 22)      # Name: Tom Age: 22
# print_person("Bob", -102)    # Invalid age

# Здесь функция print_person в качестве параметров принимает имя и возраст пользователя. Однако в функции вначале мы проверяем, соответствует ли возраст некоторому диапазону (меньше 120 и больше 0). Если возраст находится вне этого диапазона, то выводим сообщение о недопустимом возрасте и с помощью оператора return выходим из функции. После этого функция заканчивает свою работу.

# Однако если возраст корректен, то выводим информацию о пользователе на консоль.


# ФУНКЦИЯ как ТИП, ПАРАМЕТР и РЕЗУЛЬТАТ другой функции

# Функция как тип
# В Python функция фактически представляет отдельный тип. Так мы можем присвоить переменной какую-нибудь функцию и затем, используя переменную, вызывать данную функцию. Например:

# def say_hello(): 
#     print("Hello")
# def say_goodbye(): 
#     print("Good Bye")

# message = say_hello
# message()    # Hello
# message = say_goodbye
# message()    # Good Bye

# В данном случае переменной message присваивается одна из функций. Сначала ей передается функция say_hello():

# message = say_hello

# После этого переменная message будет указывать на данную функцию, то есть фактически представлять функцию say_hello. А это значит, что мы можем вызывать переменную message как обычную функцию.

# Фактически это приведет к выполнению функции say_hello, и на консоль будет выведена строка "Hello". Затем подобным образом мы можем передать переменной message другую функцию и вызвать ее.

# Подобным образом можно через переменную вызывать функцию с параметрами и возвращать ее результат:

# def sum(a, b): return a + b
# def multiply(a, b): return a * b

# operation = sum
# result = operation(5, 6)
# print(result)                # 11

# operation = multiply
# print(operation(5, 6))       # 30

# Функция как ПАРАМЕТР функции

# Поскольку функция в Python может представлять такое же значение как строка или число, соответственно мы можем передать ее в качестве параметра в другую функцию. Например, определим функцию, которая выводит на консоль результат некоторой операции:

# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")

# def sum(a, b): return a + b
# def multiply(a, b): return a * b

# do_operation(5, 4, sum)      # result = 9
# do_operation(5, 4, multiply) # result = 20

# В данном случае функция do_operation имеет три параметра, причем третий параметр, как предполагается, будет представлять функцию, которая принимает два параметра и возвращает некоторый результат. Иными словами третий параметр - operation представляет некоторую операцию, но на момент определения функции do_operation мы точно не знаем, что это будет за операция. Мы только знаем, что она принимает два параметра и возвращает какой-то результат, который потом выводится на консоль.

# При вызове функции do_operation мы сможем передать в качестве третьего параметра другую функцию, например, функцию sum:

# do_operation(5, 4, sum)

# То есть в данном случае параметр operation фактически будет представлять функцию sum и будет возвращать сумму дву чисел.

# Затем аналогичным образов в вызов функции do_operation можно передать третьему параметру другую функцию - multiply, которая выполнит умножение чисел:

# do_operation(5, 4, multiply)   # result = 20

# Таким образом, более гибкие по функциональности функции, которые через параметры принимают другие функции.


# ФУНКЦИЯ как РЕЗУЛЬТАТ функции

# Также одна функция в Python может возвращать другую функцию. Например, определим функцию, которая в зависимости от значения параметра возвращает ту или иную операцию:

# def sum(a, b): return a + b
# def subtract(a, b): return a - b
# def multiply(a, b): return a * b

# def select_operation(choice):
#     if choice == 1:
#         return sum
#     elif choice == 2:
#         return subtract
#     else:
#         return multiply

# operation = select_operation(1)      # operation = sum
# print(operation(10, 6))              # 16

# operation = select_operation(2)      # operation = subtract
# print(operation(10, 6))              # 4

# operation = select_operation(3)      # operation = multiply
# print(operation(10, 6))              # 60

# В данном случае функция select_operation в зависимости от значения параметра choice возвращает одну из трех функций - sum, subtract и multiply. Затем мы мы можем получить результат функции select_operation в переменную operation:

# operation = select_operation(1)
# Так, в данном случае в функцию select_operation передается число 1, соответственно она будет возвращать функцию sum. Поэтому переменная operation фактически будет указывать на функцию sum, которая выполняет сложение двух чисел:

# print(operation(10, 6))         # 16 - фактически равно sum(10, 6)
# Аналогичным образом можно получить и выполнить другие функции.


# ЛЯМБДА-выражения
# - ЭТО небольшие анонимные функции, которые определяются с помощью оператора lambda. Формальное определение лямбда-выражения:

# lambda [параметры] : инструкция

# Определим простейшее лямбда-выражение:

# message = lambda: print("hello")
# message()   # hello

# Здесь лямбда-выражение присваивается переменной message. Это лямбда-выражение не имеет параметров, ничего не возвращает и просто выводит строку "hello" на консоль. И через переменную message мы можем вызвать это лямбда-выражение как обычную функцию. Фактически оно аналогично следующей функции:

# def message(): 
#     print("hello")

# Если лямбда-выражение имеет параметры, то они определяются после ключевого слова lambda. Если лямбда-выражение возвращает какой-то результат, то он указывается после двоеточия. Например, определим лямбда-выражение, которое возвращает квадрат числа:

# square = lambda n: n * n

# print(square(4))    # 16
# print(square(5))    # 25

# В данном случае лямбда-выражение принимает один параметр - n. Справа от двоеточия идет возвращаемое значение - n* n. Это лямбда-выражение аналогично следующей функции:
# def square2(n): return n * n

# Аналогичным образом можно создавать лямбда-выражения, которые принимают несколько параметров:

# sum = lambda a, b: a + b

# print(sum(4, 5))    # 9
# print(sum(5, 6))    # 11

# Хотя лямбда-выражения позволяют немного сократить определения функций, тем не менее они ограничены тем, что они могут выполнять только одно выражение. Однако они могут быть довольно удобны в тех случаях, когда необходимо использовать функцию для передачи в качестве параметра или возвращения в другой функции. Например, передача лямбда-выражения в качестве параметра:

# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")

# do_operation(5, 4, lambda a, b: a + b)  # result = 9
# do_operation(5, 4, lambda a, b: a * b)  # result = 20

# В данном случае нам нет необходимости определять функции, чтобы передать их в качестве параметра, как в прошлой статье.

# То же самое касается и возвращение лямбда-выражений из функций:

# def select_operation(choice):
#     if choice == 1:
#         return lambda a, b: a + b
#     elif choice == 2:
#         return lambda a, b: a - b
#     else:
#         return lambda a, b: a * b

# operation = select_operation(1)  # operation = sum
# print(operation(10, 6))  # 16

# operation = select_operation(2)  # operation = subtract
# print(operation(10, 6))  # 4

# operation = select_operation(3)  # operation = multiply
# print(operation(10, 6))  # 60


# def minimal(l):
#     min_number = l[0]
#     for el in l:
#         if el < min_number:
#             min_number = el
#     return min_number
    

# num1 = [2, 9, 4, 6, 3, 1]
# min1 = minimal(num1)
# print(min1)
# num2 = [6, 5, 2, 1.1, 10, 9, 0.5]
# min2 = minimal(num2)
# print(min2)
# if min1 < min2:
#     print(f'Absolutly minimum:  {min1}')
# else:
#     print(f'Absolutly minimum:  {min2}')
