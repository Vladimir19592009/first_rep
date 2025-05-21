# Упражнение 2. Приветствие

# Напишите программу, запрашивающую у пользователя его имя. В ответ на ввод на экране должно появиться приветствие с обращением по имени, введенному с клавиатуры ранее.

# name = input("Yuor name? ")

# print(f"Hello, {name}!")
# Hello, Vladimir!


# Упражнение 3. Площадь комнаты

# Напишите программу, запрашивающую у пользователя длину и ширину комнаты. После ввода значений должен быть произведен расчет площади комнаты и выведен на экран. Длина и ширина комнаты должны вводиться в формате числа с плавающей запятой. Дополните ввод и вывод единицами измерения, принятыми в вашей стране. Это могут быть футы или метры.

# length = float(input("Enter length of room "))
# width = float(input("Enter width of room "))
# area_room = length * width
# print(f"Area room is {area_room} square meters ")
# Enter length of room 6
# Enter width of room 4
# Area room is 24.0 square meters


# Упражнение 4. Площадь садового участка

# Создайте программу, запрашивающую у пользователя длину и ширину садового участка в футах. Выведите на экран площадь участка в акрах: (Подсказка: В одном акре содержится 43 560 квадратных футов)

# gp_length = float(input("Enter garden plot length "))
# gp_width = float(input("Enter garden plot width "))

# gp_area = (gp_length * gp_width) / 43560
# print(f"Garden plot square is {gp_area:^10,.2f}")
# Enter garden plot length 450
# Enter garden plot width 350
# Garden plot square is    3.62


# Упражнение 5. Сдаем бутылки

# Во многих странах в стоимость стеклотары закладывается определенный депозит, чтобы стимулировать покупателей напитков сдавать пустые бутылки. Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутылки большего объема – $0,25.
# Напишите программу, запрашивающую у пользователя количество бутылок каждого размера. На экране должна отобразиться сумма, которую можно выручить, если сдать всю имеющуюся посуду. Отформатируйте вывод так, чтобы сумма включала два знака после запятой и дополнялась слева символом доллара.

# num_small_bottle = int(input("Enter the number of small bottles "))
# num_large_bottle = int(input("Enter the number of large bottles "))
# cost_of_sm = 0.1
# cost_of_lb = 0.25

# total_sales = num_small_bottle * cost_of_sm + num_large_bottle * cost_of_lb
# print(f"Total revenue will be: ${total_sales:.2f}")
# Enter the number of small bottles 50
# Enter the number of large bottles 60
# Total revenue will be: $20.00


# Упражнение 6. Налоги и чаевые

# Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане. После этого должен быть произведен расчет налога и чаевых официанту. Вы можете использовать принятую в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве чаевых мы оставим 18 % от стоимости заказа без учета налога. На выходе программа должна отобразить отдельно налог, сумму чаевых и итог, включая обе составляющие. Форматируйте вывод таким образом, чтобы все числа отображались с двумя знаками после запятой.

# SALES_TAX = 0.05
# TIP = 0.18
# restaurant_order = float(input("How much (number) was the order in the restaurant? "))

# sum_tax = SALES_TAX * restaurant_order
# sum_tip = TIP * restaurant_order
# total_sum = restaurant_order + sum_tax + sum_tip

# print(f" Налог составит: ${sum_tax:.2f} \n Чаевые: \t ${sum_tip:.2f} \n Полные затраты: ${total_sum:.2f}")
# How much (number) was the order in the restaurant? 250
#  Налог составит: $12.50
#  Чаевые:         $45.00
#  Полные затраты: $307.50


# Упражнение 7. Сумма первых n положительных чисел

# Напишите программу, запрашивающую у пользователя число и подсчитывающую сумму натуральных положительных чисел от 1 до введенного пользователем значения. Сумма n положительных чисел может быть рассчитана по формуле:     sum = n*(n+1)/2

# your_num = int(input("Enter natural positive namber: "))

# sum_namber = your_num * (your_num +1) / 2
# print(sum_namber)
# Enter natural positive namber: 55
# 1540.0


# Упражнение 8. Сувениры и безделушки

# Интернет-магазин занимается продажей различных сувениров и безделушек. Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите программу, запрашивающую у пользователя количество тех и других покупок,после чего выведите на экран общий вес посылки.

# souvenir = 0.075
# knickknack = 0.112
# count_souv = int(input("Enter number of souvenirs: "))
# count_knick = int(input("Enter number of knickknacks: "))

# total_weight = count_souv * souvenir + count_knick * knickknack
# print(f"Общий вес посылки: {total_weight:.3f} кг")
# Enter number of souvenirs: 23
# Enter number of knickknacks: 16
# Общий вес посылки: 3.517 кг


# Упражнение 9. Сложные проценты

# Представьте, что вы открыли в банке сберегательный счет под 4 % годовых. Проценты банк рассчитывает в конце года и добавляет к сумме счета. Напишите программу, которая запрашивает у пользователя сумму первоначального депозита, после чего рассчитывает и выводит на экран сумму на счету в конце первого, второго и третьего годов. Все суммы должны быть округлены до двух знаков после запятой.

# your_deposit = int(input("Какую сумму хотите положить на депозит? "))
# deposit_interest = 0.04

# amount_acc1 = your_deposit + your_deposit * deposit_interest
# print(f"После первого года сумма на счету: ${amount_acc1:.2f}")
# # После первого года сумма на счету: $4160000.00

# amount_acc2 = amount_acc1 + amount_acc1 * deposit_interest
# print(f"После второго года сумма на счету: ${amount_acc2:.2f}")
# # После второго года сумма на счету: $4326400.00

# amount_acc3 = amount_acc2 + amount_acc2 * deposit_interest
# print(f"После третьего года сумма на счету: ${amount_acc3:.2f}")
# # После третьего года сумма на счету: $4499456.00


# Упражнение 11. Потребление топлива

# В США потребление автомобильного топлива исчисляется в милях на галлон (miles-per-gallon – MPG). В то же время в Канаде этот показатель обычно выражается в литрах на 100 км (liters-per-hundred kilometers –L/100 km). Используйте свои исследовательские способности, чтобы определить формулу перевода первых единиц исчисления в последние. После этого напишите программу, запрашивающую у пользователя показатель потребления топлива автомобилем в американских единицах и выводящую его на экран в канадских единицах.
# 1 галон = 3,785 литра
# 1 миля = 1,60934 км


# dist_miles = float(input("Enter distance travelled in miles "))
# fuel_halons = float(input("Enter fuel consumption in halons "))
# MPG = dist_miles / fuel_halons

# l_per_100km = (100 * 3.785)/ (MPG * 1.60934)
# print(f"Fuel consumption in liters per-hundred kilometers {l_per_100km:.2f} L/100km")
# Enter distance travelled in miles 100
# Enter fuel consumption in halons 4
# Fuel consumption in liters per-hundred kilometers 9.41 L/100km
