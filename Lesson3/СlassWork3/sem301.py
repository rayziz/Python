
# Задача 1
# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

import random
from random import randint

N = 6

# def rand_list(N:int):
lst = []
for i in range(N):
    lst.append(randint(-N, N))
print(lst)

number_mult = randint(1, N)
with open ('file_sem_301_1.txt', 'w') as data:
    for i in range (number_mult):
        data.writelines(str(randint(0, N - 1)) + '\n')

indexes_list = []
with open ('file_sem_301_1.txt', 'r') as data:
    for str in data:
        indexes_list.append(int(str[:-1]))
print(indexes_list)


mult = 1
for i in indexes_list:
    mult *= lst[i]

print(mult)


# Задача 2
# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# k = 8

# fib_right = []
# for i in range(k + 1):
#     el = i if i == 0 or i == 1 else fib_right[i - 1] + fib_right[i - 2]
#     fib_right.append(el)

# fib_left = []
# for i in range(k + 1):
#     el = i if i == 0 or i == 1 else fib_left[i - 2] - fib_left[i - 1]
#     fib_left.append(el)

# fib_left.reverse()

# fib_list = fib_left + fib_right[1:]

# print(fib_list)


# Задача 3
# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

# string = '34 56 74 87 345'

# string_to_number = list(map(int, string.split(' ')))
# print(f'В списке {string} макс чилло {max(string_to_number)}, при этом мин {min(string_to_number)} ')
# print(min(string))