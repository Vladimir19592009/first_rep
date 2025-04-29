
#13. СПИСКИ - операторы и функции работы с ними
# (https://www.youtube.com/watch?v=HgFGVQG20Oc&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd&index=13)

# список - упорядоченная изменяемая коллекция данных и могут содержать все возможные типы данных
# метод len()
# lst = ['Moscow', 2034, 5.8, True, [1, 2, 3], (5, 6, 7), {1: 'Alice', 2: 'Bob'}]
# print(len(lst))   # 7
# print(lst[4][1])  # 2  (в четвёртом (по индексу) элементе списка lst находим первый (по индексу) элемент)
# print(lst[5][0])  # 5  (в пятом (по индексу) элементе списка lst находим нулевой (по индексу) элемент)
# print(lst[6][1])  # Alice  (в шестом (по нидексу) элементе списка lst достаём значение по ключу)

# метод max()
# метод min()
# метод sum()
# метод sorted()

# ls1 = ['Moscow', 2034, 5.8, True]
# ls2 = [3, 5, 6]


# (+) соединение двух списков в один
# print(ls1 + ls2)  # ['Moscow', 2034, 5.8, True, 3, 5, 6]

# (*) дублирование списка
# print(ls1 * 2)  # ['Moscow', 2034, 5.8, True, 'Moscow', 2034, 5.8, True]

# (in) проверка вхождения элемента в список
# print('Moscow' in ls1)  # True

# del удаление элемента списка
# del ls1[1]
# print(ls1)  # ['Moscow', 5.8, True]



#14. СРЕЗЫ списков и сравнение списков
# (https://www.youtube.com/watch?v=Vx3s01Yb1P8&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd&index=14)

