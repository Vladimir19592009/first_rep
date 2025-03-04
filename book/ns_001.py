# Глава 8. (стр 436) Подробнее о строковых данных

# Доступ к отдельным символам и строковым значениям  возможен при применении цикла for и индексации:

# Один из самых простых способов получить доступ к отдельным символам в строковом зна­чении состоит в применении цикла for.

# for переменная in строковое_значение:
#   инструкция
#   инструкция

#  Во время каждой ите­рации цикла переменная будет ссылаться на копию символа в строковом значении, начиная с первого символа. Мы говорим, что цикл выполняет последовательный перебор символов в строковом значении.
'''
name = 'Джулия'
for ch in name:
    print (ch)
# Д
# ж
# y
# л
# и
# я
'''
# В программе 8.1 приведен еще один пример. Эта программа просит пользователя ввести строковое значение. Затем она применяет цикл for для обхода строкового значения, подсчи­тывая количество появлений буквы Т (в верхнем или нижнем регистре). Предположим будет введено предложение: " Кто не ходит, тот и не падает."
'''
def main():
    # Для подсчёта кол-ва букв создадим переменную:
    count = 0
    my_string = input('Enter offer: ')
    for ch in my_string.lower():
        if ch == 'т':
            count += 1
    print(count)
if __name__ == '__main__':
    main()
# 5
'''
# Индексация

# Еще один способ получить доступ к отдельным символам в строковом значении реализуется при помощи индекса. Каждый символ в строковом значении имеет индекс, который задает его позицию. Индексация начинается с О, поэтому индекс первого символа равняется О, ин­декс второго символа равняется 1 и т. д. Индекс последнего символа в строковом значении равняется количеству символов в строковом значении минус 1.
'''
my_string = 'Ромашки белые'
ch = my_string[6]
print(ch)
# и
print(my_string[-1], my_string[-2], my_string[-13])
# e ы P
print(my_string[-14])
# IndexError
'''
# Функция len

# В главе 7 вы познакомились с функцией len, которая возвращает длину последовательности. Функция len также используется для получения длины строкового значения.
'''
city = 'Бостон'
size = len (city)
print(size)
# 6
'''
# Функция len в особенности полезна для предотвращения ситуаций, когда циклы заходят запределы конца строкового значения с получением IndexError:
'''
city = 'Бостон'
index = 0
while index < len(city):
    index += 1
print(index)
# 6
'''
# Конкатенация строковых данных

# конка­тенация, или присоединение одного строкового значения в конец другого.

# Оператор + порождает строковое значение, которое является объединением двух других строковых значений, используемых в качестве его операндов.
'''
first_name = 'Emily'
last_name = 'Egger'
full_name = first_name + ' ' + last_name
print(full_name)
# Emily Egger
'''
# Для выполнения конкатенации можно также использовать оператор +=.
'''
letters = 'asdf'
letters += '1234'
print(letters)
# asdf1234
'''
# Следует иметь в виду, что операнд с левой стороны от оператора+= должен быть существующей переменной. Если указать несуществующую переменную, то будет вызвано исклю­чение.

# Строковые данные как немутируемые последовательности

# В Python данные строкового типа являются немутируемыми последовательностями, т. е. по­сле создания их нельзя изменить. Некоторые операции, такие как конкатенация, производят впечатление, что они видоизменяют строковые данные, но в действительности этого не про­исходит. Значения литералов как были так и остались в неприкосновенности. Произошло лишь соединение литералов и переприсваивание переменной нового значения.


# МЕТОДЫ ПРОВЕРКИ СТРОКОВЫХ ЗНАЧЕНИЙ

# БУЛЕВЫЕ: (начинются на is)

#  метод isdigit() возвращает True, если строковое зна­чение содержит только цифры. В противном случае он возвращает False.

# isalpha() Возвращает True, если строковое значение содержит только буквы алфавита и имеет по крайней мере один символ. В противном случае возвращает False

# isalnum() Возвращает True, если строковое значение содержит только буквы алфавита или цифры и имеет по крайней мере один символ. В противном случае возвращает False

# islower () Возвращает True, если все буквы алфавита в строковом значении находятся в нижнем регистре, и строковая последовательность содержит по крайней мере одну букву алфавита.В противном случае возвращает False

# isspace() Возвращает True, если строковое значение содержит только пробельные символы и имеет по крайней мере один символ. В противном случае возвращает False. (Пробельными символами являются пробелы, символы новой строки (\n) и символы табуляции (\t).)

# isupper() Возвращает True, если все буквы алфавита в строковом значении находятся в верхнем регистре, и строковая последовательность содержит по крайней мере одну букву алфавита. В противном случае возвращает False


# МЕТОДЫ МОДИФИКАЦИИ СТРОКОВЫХ ЗНАЧЕНИЙ:

# Несмотря на то что строковые данные являются немутируемыми последовательностями, т. е. их нельзя изменить, они имеют много методов, которые возвращают их видоизмененные версии:

# lower() Возвращает копию строкового значения, в котором все буквы преобразованы в нижний регистр . Любой символ, который уже находится в нижнем регистре или не является буквой алфавита, остается без изменения.

# lstrip() Возвращает копию строкового значения, в котором все ведущие пробельные символы удалены. Ведущими пробельными символами являются пробелы, символы новой строки (\n) и символы табуляции (\t), которые появляются в начале строкового значения

# lstrip(символ) Аргументом <символ> является строковое значение, содержащее символ. Возвращает копию строкового значения, в котором удалены все экземпляры символа, появляющиеся в начале(left слева) строкового значения.

# rstrip() Возвращает копию строкового значения, в котором все замыкающие пробельные символы удалены. Замыкающими пробельными символами являются пробелы, символы новой строки (\n) и символы табуляции(\t), которые появляются в конце строкового значения.

# rstrip(символ) Аргументом <символ> является строковое значение, содержащее символ. Возвращает копию строковой последовательности, в которой удалены все экземпляры символа, появляющиеся в конце строкового значения.

# strip() Возвращает копию строкового значения, в котором удалены все ведущие и замыкающие пробельные символы.

# strip(символ) Возвращает копию строкового значения, в котором удалены все экземпляры символа, появляющиеся в начале и конце строкового значения.

# upper() Возвращает копmо строкового значения, в котором все буквы преобразованы в верхний регистр . Любой символ, который уже находится в верхнем регистре или не является буквой алфавита, остается без изменения.


# МЕТОДЫ ПОИСКА И ЗАМЕНЫ:

# выполняют поиск подстрок, а также метод, который заменяет найденные подстроки другой подстрокой.

# andswith(подстрока) Аргумент <подстрока> это строковое значение. Метод возвращает истину, если строковое значение заканчивается подстрокой.

# find(подстрока) Аргумент <подстрока> это строковое значение. Метод возвращает наименьший индекс в строковом значении, где найдена подстрока. Если подстрока не найдена, метод возвращает -1.

# replace(старое, новое) Аргументы <старое и новое> - это строковые значения. Метод возвращает копию строкового значения, в котором все экземпляры старых подстрок заменены новыми подстроками.

# startswith(подстрока) Аргумент подстрока - это строковое значение. Метод возвращает истину, если строковое значение начинается с подстроки.

# МЕТОД .count().

# Метод .count(substring) возвращает количество не пересекающихся вхождений подстроки substring в строке.
# Пример строки: Подсчитаем количество вхождений буквы 'o'
'''
text = "hello world, hello universe!"  
count_o = text.count('o')  
print("Количество 'o' в строке:", count_o)  # Вывод: 2
'''
# Подсчитаем количество вхождений слова 'hello'
'''
count_hello = text.count('hello')  
print("Количество 'hello' в строке:", count_hello)  # Вывод: 2  
'''

# ОПЕРАТОР ПОВТОРЕНИЯ:

# копируемое_ с троковое_ значение * n

# Например:
'''
my_string = 'w' * 5
print(my_string)
# wwwww
'''
# Программа 8.8 демонстрирует оператор повторения:
'''
def main():
    for count in range(1, 4):
        print('z' * count)
    for count in range(4, 0, -1):
        print('z' * count)
if __name__ == '__main__':
    main()
# z
# zz
# zzz
# zzzz
# zzz
# zz
# z
'''


# РАЗБИЕНИЕ СТРОКОВОГО ЗНАЧЕНИЯ: методом:

# split() метод возвращает список, стоковых значений.

# В программе 8.9 приведен пример:
'''
def main():
    my_string = 'One Two Three Four'
    word_list = my_string.split()
    print(word_list)
if __name__ == '__main__':
    main()
# ['One', 'Two', 'Three', 'Four']
'''
'''
date_string = '26/11/2020'
date_list = date_string.split('/')
'''
# print(date_list)
# ['26', '11', '2020']
'''
print(f'Day: {date_list[0]}')
print(f'month: {date_list[1]}')
print(f'Year: {date_list[2]}')
'''
# Day: 26
# month: 11
# Year: 2020


# СТРОКОВЫЕ ЛЕКСЕМЫ:

# В Python для лексемизации строк используется метод split(). Програм­ма 8.11 демонстрирует его работу:
'''
def main():
    str1 = 'One Two Three'
    str2 = '10:20:30'
    str3 = 'a/b/c'
    
    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')
    print()    

def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for i in tokens:
        print(f'Leksem: {i}')
if __name__ == '__main__':
    main()
# Leksem: One
# Leksem: Two
# Leksem: Three
# Leksem: Three

# Leksem: 10
# Leksem: 20
# Leksem: 30

# Leksem: a
# Leksem: b
# Leksem: c
'''

# Глава 8. УПРАЖНЕНИЯ ПО ПРОГРАММИРОВАНИЮ:

# 1. ИНИЦИАЛЫ. Напишите программу, которая получает строковое значение, содержащее имя, отчество и фамилию человека и показывает инициалы. Например, если пользователь вводит Михаил Иванович Кузнецов, то программа должна вывести М.И.К.
'''
person = input('Введите ФИО полностью: ')
word_pers = person.split()

# Проверяем, что введено три части (имя, отчество, фамилия)  
if len(word_pers) == 3:
    # Вычисляем первые буквы персоны
    leter_pers = [i[0] for i in word_pers]
    leter_pers_dots = '.'.join(leter_pers) + '.'
    print(leter_pers_dots)
else:
    print( "Введите полное имя, состоящее из имени, отчества и фамилии.")
# M.И.K.
'''
# 2. СУММА ЧИСЕЛ В СТРОКЕ. Напишите программу, которая просит пользователя ввести ряд однозначных чисел без разделителей. Программа должна вывести на экран сумму всех однозначных чисел в строковом значении. Например, если пользователь вводит 2514, то этот метод должен вернуть значение 12, которое является суммой 2, 5, 1 и 4.
'''
my_num = input('Enter arbitrary number: ')
total_sum = 0
for ch in my_num:
    if ch.isdigit():
        total_sum += int(ch)  # Приводим символ к целочисленному типу и добавляем к сумме
    else:
        print('Введите только однозначные числа.')
print(total_sum)
# 12
'''
# 3. ПРИНТЕР ДАТ. Напишите программу, которая считывает от пользователя строковое зна­чение, содержащее дату в формате дд/MМ/гггг. Она должна напечатать дату в формате 26 декабря 2025 г.
'''
date_sting = '26/12/2025'
date_list = date_sting.split('/')

month_string = 'январь февраль март апрель май июнь июль август сентябрь октябрь ноябрь декабрь'
month_list = month_string.split(' ')

print(date_list[0] + ' ' + month_list[12 - 1] + ' ' + date_list[2])
# 26 декабрь 2025
'''
# 5. Алфавитный переводчик номера телефона. Многие ·компании используют телефонные номера наподобие 555-GET-FOOD, чтобы клиентам было легче запоминать эти номера. На стандартном телефоне буквам алфавита поставлены в соответствие числа. Напишите программу, которая просит пользователя ввести 1О-символьный номер теле­фона в формате ХХХ-ХХХ-ХХХХ. Приложение должно показать номер телефона, в ко­тором все буквенные символы в оригинале переведены в их числовой эквивалент. Например, если пользователь вводит 555-GET-FOOD, то приложение должно вывести 555-438-3663. Используйте строки:

# ----------------------------------------------------
# С ипользованием словаря:
'''
def translate_phone_number(phone_number):  
    # Создаем словарь для перевода букв в цифры  
    letter_to_digit = {  
        'A': '2', 'B': '2', 'C': '2',  
        'D': '3', 'E': '3', 'F': '3',  
        'G': '4', 'H': '4', 'I': '4',  
        'J': '5', 'K': '5', 'L': '5',  
        'M': '6', 'N': '6', 'O': '6',  
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',  
        'T': '8', 'U': '8', 'V': '8',  
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'  
    }  
    
    # Переводим номер  
    translated_number = ""  
    for char in phone_number:  
        if char.isalpha():  # Если символ - буква  
            translated_number += letter_to_digit[char.upper()]  # Добавляем соответствующую цифру  
        else:  
            translated_number += char  # Добавляем символ как есть (цифры и дефисы)  
    
    return translated_number  

# Запрашиваем ввод от пользователя  
user_input = input("Введите номер телефона в формате ХХХ-ХХХ-XXXX: ")  
translated = translate_phone_number(user_input)  
print("Переведенный номер телефона:", translated)  
# 555-438-3663
'''
# ----------------------------------------------------

# Без использования словаря:

'''
def translate_phone_number(phone_number):
    translated_number = ""

    for char in phone_number:
        if char.isdigit() or char == '-':  # Если символ - цифра или дефис
            translated_number += char
        elif char.isalpha():  # Если символ - буква
            # Переводим буквы в цифры по группам
            if char.upper() in "ABC":
                translated_number += '2'
            elif char.upper() in "DEF":
                translated_number += '3'
            elif char.upper() in "GHI":
                translated_number += '4'
            elif char.upper() in "JKL":
                translated_number += '5'
            elif char.upper() in "MNO":
                translated_number += '6'
            elif char.upper() in "PQRS":
                translated_number += '7'
            elif char.upper() in "TUV":
                translated_number += '8'
            elif char.upper() in "WXYZ":
                translated_number += '9'

    return translated_number


# Запрашиваем ввод от пользователя
user_input = input("Введите номер телефона в формате ХХХ-ХХХ-XXXX: ")
translated = translate_phone_number(user_input)
print("Переведенный номер телефона:", translated)
# 555-438-3663
'''
# ----------------------------------------------------

# 10. Самый частотный символ. Напишите программу, которая предоставляет пользователю возможность ввести строковое значение и выводит на экран символ, который появляется в нем наиболее часто.

'''
def most_frequent_character(input_string):
    # Удаляем пробелы для более удобного анализа
    input_string = input_string.replace(" ", "")
    input_string = input_string.lower()

    # Создаем словарь для подсчета частоты символов
    frequency = {}

    # Подсчитываем частоту каждого символа
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Находим символ c максимальной частотой
    max_count = 0
    most_frequent_char = ""

    for char, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent_char = char

    return most_frequent_char, max_count


# Запрашиваем ввод от пользователя
user_input = input("Введите строку: ")

# Находим самый частый символ
result_char, result_count = most_frequent_character(user_input)

# Выводим результат
print(f"Самый частый символ: '{result_char}' (встречается {result_count} раз)")
# зависит от вводимой строки
'''
# 11. Разделитель слов. Напишите программу, которая на входе принимает предложение, в котором все слова написаны без пробелов, но первая буква каждого слова находится в верхнем регистре. Преобразуйте предложение в строковое значение, в котором слова отделены пробелами, и только первое слово начинается с буквы в верхнем регистре. На­пример, строковое значение "ОстановисьИПочувствуйЗапахРоз" будет преобразовано в "Остановись и почувствуй запах роз".


def split_camel_case(sentences):
    words = []  # ['Остановись', 'И', 'Почувствуй', 'Запах', 'Роз']
    current_word = ""

    for char in sentence:
        # Если символ заглавный и текущая строка не пуста, то значит, мы нашли новое слово
        if char.isupper() and current_word:
            words.append(current_word)
            current_word = char  # Начинаем новое слово
        else:
            current_word += char  # Добавляем символ к текущему слову

    # Не забудьте добавить последнее слово
    if current_word:
        words.append(current_word)

    words = words[0] + ' ' + words[1] + ' ' + \
        words[2] + ' ' + words[3] + ' ' + words[4] + '.'
    words = words.lower()
    words = words.capitalize()

    return words

# Пример использования
sentence = "ОстановисьИПочувствуйЗапахРоз"
result = split_camel_case(sentence)
print(result)
# Остановись и почувствуй запах роз.
