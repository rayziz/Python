# 1) Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

# def sequence(n:int):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += (1+1/i)**i
#     return summa

# print(sequence(5))


# 2) Реализовать алгоритм перемешивания списка.

# Вариант 1 
# from dataclasses import replace
# import time

# random_list = [1, 2, 3, 4, 5]
# t = time.time_ns()
# tS = int(t)
# for i in range(1000):
#     t1 = int(str(time.time_ns())[-3])
#     temp = random_list.pop(t1//2)
#     random_list.append(temp)
# print(random_list)


# Вариант 2
# import random
# from random import randint

# numbers = [1, 2, 3, 4, 5]

# def random_list(list):
#     list_length = len(list)
#     for i in range(list_length):
#         index = random.randint(0, list_length - 1)

#         temp = list[i]
#         list[i] = list[index]
#         list[index] = temp
#     return list

# print(numbers)
# numbers = random_list(numbers)
# print(numbers)


# 3)  Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
# Фактически это первая часть прошлого задания


# 4) Определить, присутствует ли в заданном списке строк, 
# некоторое число

def number_contain_in_text(text, number):
    for str in text:
        if number_contain_in_str(str, number):
            print('[DEBUG]: число присутствует в строке:' + str)
            return True
    return False

def number_contain_in_str(str, number):
    if str.find(number) != -1:
        return True
    return False

number = input('Введите искомое число')

text = ["Привет1", "24 Настроение", "Настое7ние"]

print(f"Искомый список {text}")
print(f"Искомое число {number} присутствует в {number_contain_in_text(text, number)}")



# 5) Определить, позицию второго вхождения строки в списке 
# либо сообщить, что её нет.
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", 
# ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу",
#  ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу",
#  ответ: -1

# def find_second_string_in_list(words, str):
#     cnt_find = 0
#     for i in range(len(words)):
#         if words[i] == str:
#             cnt_find += 1
#             if cnt_find == 2:
#                 return i
#         return -1

# words = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
# pivot = "qwe4"
# second_index = find_second_string_in_list(words, pivot)
# print(f'Исходник {words}')
# print(f'искомаястрока {pivot}')
# print(f'позиц втор вхождения {second_index}')

# 6) Задать список из N элементов, заполненных числами из [-N, N]
# найти провизведение элементов на указанных позициях

# print('Введите N')
# N = int(input())
# print('Позиция элемента 1')
# pos1 = int(input())-1
# print('Позиция элемента 2')
# pos2 = int(input())-1

# list = []
# i = 0
# while i < N:
#     list.append(N)
#     list.append(-N)
#     i += 1
# print(list)
# result = list[pos1]*list[pos2]
# print(result)