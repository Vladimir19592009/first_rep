# Для тестирования чего-то непонятного


# Задание 1
# Напишите класс MusicAlbum, у которого есть: Атрибуты title, artist, release_year, genre, tracklist (название, исполнитель, год выхода, жанр, список треков. Метод play_random_track() для вывода случайного названия песни.

# import random


# class MusicAlbum:
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         """
#         Инициализация атрибутов альбома.

#         :param title: Название альбома
#         :param artist: Исполнитель
#         :param release_year: Год выпуска
#         :param genre: Жанр
#         :param tracklist: Список треков (список словарей c названием, исполнителем и годом выхода)
#         """
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist

#     def play_random_track(self):
#         """
#         Метод для воспроизведения случайного трека из списка треков альбома.
#         """
#         random_track = random.choice(self.tracklist)
#         print(
#             f"Сейчас играется: '{random_track['title']}' — {random_track['artist']} ({random_track['release_year']}, Жанр: {random_track['genre']})")


# # Пример использования класса
# if __name__ == '__main__':
#     album_title = "Thriller"
#     album_artist = "Michael Jackson"
#     album_release_year = 1982
#     album_genre = "Pop"
#     album_tracklist = [
#         {"title": "Wanna Be Startin' Somethin'", "artist": "Michael Jackson",
#             "release_year": 1982, "genre": "Pop"},
#         {"title": "Baby Be Mine", "artist": "Michael Jackson",
#             "release_year": 1982, "genre": "Pop"},
#         {"title": "The Girl Is Mine", "artist": "Michael Jackson",
#             "release_year": 1982, "genre": "Pop"},
#         {"title": "Thriller", "artist": "Michael Jackson",
#             "release_year": 1982, "genre": "Pop"},
#         {"title": "Beat It", "artist": "Michael Jackson",
#             "release_year": 1982, "genre": "Pop"},
#         {"title": "Billie Jean", "artist": "Michael Jackson",
#             "release_year": 1982, "genre": "Pop"},
#         {"title": "Human Nature", "artist": "Michael Jackson",
#             "release_year": 1982, "genre": "Pop"},
#         {"title": "P.Y.T. (Pretty Young Thing)", "artist": "Michael Jackson",
#          "release_year": 1982, "genre": "Pop"},
#         {"title": "The Lady in My Life", "artist": "Michael Jackson",
#             "release_year": 1982, "genre": "Pop"}
#     ]

#     album = MusicAlbum(album_title, album_artist,
#                        album_release_year, album_genre, album_tracklist)

#     # Воспроизводим случайный трек
#     album.play_random_track()

# -----------------------------------------------------------------------------------

# Программирование на Python с нуля за 8 часов (https://www.youtube.com/watch?v=jFgBUu3Bqas)

# Раздел: Введение в ООП.

# class Animal:
#     name = 'No Name'
#     age = 0
#     fed = False

#     count = 0
#     lst = []

#     def __init__(self, name, age, fed):
#         self.name = name
#         self.age = age
#         self.fed = fed
#         Animal.count += 1             # ведём подсчёт животных
#         Animal.lst.append(self.name)  # добавляем имена в список lst[]

#     def feed(self):
#         if not self.fed:
#             self.fed = True


# cat1 = Animal('Barsic', 3, True)
# cat2 = Animal('Gopen', 2, False)

# cat2.feed()     # покормим cat2, ведь он изначально не кормлен (False)
# print(cat2.fed) # принт показывает, что теперь пакормлен

# print(Animal.count)
# print(Animal.lst)

# --------------------------------------------------------------------------------

# Задание 1
# Напишите функцию для вывода треугольника. Функция принимает два аргумента – size (размер сторон треугольника) и symb (символ, используемый для заполнения треугольника).

# def drow_triangl(sise, symb):
#     for i in range(1, sise + 1):
#         print(symb * min(i, sise + 1 - i))
        
        
# sise = int(input('Введите размер: '))
# symb = input('Введите символ: ')
# drow_triangl(sise, symb)

# Задание 2
# Напишите функцию, которая принимает произвольное количество целых чисел, и возвращает среднее арифметическое без использования встроенных функции sum() и len().

def arithmetic_average(args):
    return



args = [5, 4, 3, 9, 7, 10]
arithmetic_average(args)
