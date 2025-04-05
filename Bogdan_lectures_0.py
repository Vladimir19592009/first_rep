# ТИПЫ ОБЪЕКТОВ:

# 1. НЕИЗМЕНЯЕМЫЕ: 
# string - str;  boolean - bool;  integer - int;  float;  tuple - кортеж;  None - NoneType

# 2. ИЗМЕНЯЕМЫЕ:
# list - (список - list);  dictionary - (словарь - dict);  set - (набор - set); user-defined class - (пользовательские классы).

# Посмотрим, какие идентификааторы есть подтверждающие, что перед нами объект:
# получить адрес объекта в памяти компа:

my_number = 10
print(id(my_number))
# 140732738503880

my_string = 'abc' 
print(id(my_string))
# 1848088296352

