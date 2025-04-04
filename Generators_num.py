# В Python генерация случайных чисел в заданном диапазоне осуществляется с помощью модуля `random`. Вот несколько способов использования этого модуля для генерации случайных чисел:

# 1. Генерация одного случайного числа
# Для генерации одного случайного целого числа в заданном диапазоне можно использовать функцию `randint()`. Например:

import random

# Генерация случайного целого числа от 1 до 10 (включительно)

random_number = random.randint(1, 10)
print(random_number)


# 2. Генерация нескольких случайных чисел
# Чтобы получить несколько случайных чисел из диапазона, можно использовать `sample()`. Она позволяет выбрать уникальные значения без повторений:


# Генерация 5 уникальных случайных чисел от 1 до 10

random_numbers = random.sample(range(1, 11), 5)
print(random_numbers)


# 3. Генерация случайных чисел с плавующей запятой
# Если вам нужно сгенерировать случайное число с плавающей точкой, используйте `uniform()`:


# Генерация случайного числа с плавающей запятой от 1.0 до 10.0

random_float = random.uniform(1.0, 10.0)
print(random_float)

# 4. Генерация случайных чисел в диапазоне с заданным шагом
# Для этого можно использовать функцию `randrange()`:


# Генерация случайного числа от 1 до 10 с шагом 2 (например, 1, 3, 5, 7, 9)

random_step_number = random.randrange(1, 11, 2)
print(random_step_number)

# Пример: генерация случайных чисел в диапазоне
# Вот объединённый пример, который генерирует различные типы случайных чисел:


# Генерация одного случайного целого числа

single_random = random.randint(1, 10)
print(f"Случайное целое число: {single_random}")

# Генерация массива уникальных случайных чисел

unique_randoms = random.sample(range(1, 11), 5)
print(f"Уникальные случайные числа: {unique_randoms}")

# Генерация случайного числа с плавающей запятой

float_random = random.uniform(1.0, 10.0)
print(f"Случайное число c плавающей запятой: {float_random}")

# Генерация случайного числа с заданным шагом

step_random = random.randrange(1, 11, 2)
print(f"Случайное число c шагом: {step_random}")

# Заключение
# Эти примеры позволят вам начать использовать генерацию случайных чисел в Python. Если у вас есть специфические требования или вопросы о том, как использовать эти функции, дайте знать!
