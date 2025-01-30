# СТРОКИ (Методы строк)
# https://pylot.me/article/ed0-shpargalka-po-strokam-str-v-python/#Metody-strok

cmd = "interface Gi0/0"

print(len(cmd))
# 15 (ф-ия 'len' возврвщает кол. элементов в строке)
print(len("\n abc"))
# 5 (возвращает 5 т.к. \n считается за ОДИН элемент)
print(len("\nabc"))
# 4

print(cmd.upper())
# INTERFACE GI0/0 (возвращает в вехнем регистре)
print(cmd.lower())
# interface gi0/0 (возвращает в нижнем регистре)

print(cmd.startswith("interface"))
# True (если стр. начинается с этого слова (строкой))
print(cmd.endswith("test"))
# False (если стр. заканчивается этим словом (строкой))
print(cmd.count("e"))
# 2 (в cmd буква "е" встречается 2 раза)

# Два способа получения результата:
a = "Hello"
b = "world"
print(a, b)
print(a + " " + b)
# Hello world

# Метод find (найти):

print(cmd.find("face"))
# 5 (возврат индекса с которого начинается подстрока)
print(cmd.find("test"))
# -1 (выводится в случае если подстрока не обнаружена)

# Еще пример:
cmd = " switchport mode access"
find_word = "mode"
print(cmd.find(find_word))
# 12
index = cmd.find(find_word)
print(cmd[index:])
# mode access
print(cmd[index:index + len(find_word)])
# mode

# Метод replace - замещает в стоке указанные элементы

# Пример:
cmd = "interface Gi0/0"
print(cmd.replace("i", "TEST"))
# TESTnterface GTEST0/0
cmd = "interface Gi0/0"
print(cmd.replace("i", "TEST", 1))
# TESTnterface Gi0/0 (замещение произошло только в одном месте)

# Теперь паровозик:
print(cmd.replace("Gi", "Fa").replace("0", "255").replace("face", "CACE"))
# interCACE Fa255/255

# Метод strip удаляет все спецсимволы в начале и в конце стоки.
# lstrip (rstrip) удаляет слева (справа) т.с.

# Пример:
cmd = "\n\n interface Gi0/0 \n \t"
print(cmd.strip())
# interface Gi0/0 (осталась чистая строка)

# Метод split из длинной не "причесанной" строки содаёт "правильный" [список] 'строк'.

# Пример:
cmd = " switchport mode access\n vlan 1,2,3,4,5 \n"
print(cmd.split())
# ['switchport', 'mode', 'access', 'vlan', '1,2,3,4,5']

# Пример:
vlan = "1,2,3,4,5"
print(vlan.split(","))
# ['1', '2', '3', '4', '5']
ip = "10.1.1.1"
print(ip.split("."))
# ['10', '1', '1', '1']
