# ТИПЫ ОБЪЕКТОВ:

# 1. НЕИЗМЕНЯЕМЫЕ:
# string - str;  boolean - bool;  integer - int;  float;  tuple - кортеж;  None - NoneType

# 2. ИЗМЕНЯЕМЫЕ:
# list - (список - list);  dictionary - (словарь - dict);  set - (набор - set); user-defined class - (пользовательские классы).

# Посмотрим, какие идентификааторы есть подтверждающие, что перед нами объект:
# получить адрес объекта в памяти компа:

# my_number = 10
# print(id(my_number))
# # 140732738503880

# my_string = 'abc'
# print(id(my_string))
# # 1848088296352


# drinks = ["chocolate", "coffee", "decaf"]
# flavors = ["caramel", "vanilla", "peppermint", "raspberry", "plain"]
# toppings = ["chocolate", "cinnamon", "caramel"]


# import random


# def guessing_game():
#     answer = random.randint(0, 100)

#     while True:
#         user_guess = int(input("Каковы ваши предположения? "))
#         if user_guess == answer:
#             print(f"Правильно! Ответ {user_guess}")
#             break
#         if user_guess < answer:
#             print(f"Ваше число {user_guess} слишком маленькое!")
#         else:
#             print(f"Ваше число {user_guess} слишком большое!")


# guessing_game()
