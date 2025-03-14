# Для тестирования чего-то непонятного

# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
tom = Person('Tom', 22)
print(tom.name)
print(tom.age)

tom.age = 37
print(tom.age)

