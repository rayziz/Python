# Задча 1. Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
# Готово

# N = -3
# power = int(input('Введите степень числа = '))
# print((N)**power)

# Задача 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# Готово
# def dictionary(n:int):
#     number = {}
#     for i in range(1, n + 1):
#         number[i] = (3 * i) + 1
#     print(number)

# dictionary(9)

# Задача 3. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
#Готово

# def str_counter(str1:str, str2:str):
#     str1, str2 = max([str1, str2], key=len), min([str1, str2], key=len)
#     count = 0
#     checking_area_len = len(str2)
#     for i in range(len(str1)):
#         checking_area = str1[i:i + checking_area_len]
#         if checking_area == str2:
#             count += 1
#     return count

# str1 = 'Как Вы могли понять я сдаю это ДЗ с достаточно большим опозданием))'
# str2 = ')'

# print(str_counter(str1, str2))

#решение 2 короткое

# str1 = 'Как Вы могли понять я сдаю это ДЗ с достаточно большим опозданием))'
# str2 = ')'
# count = str1.count(str2)
# print(count)


# Задача 4. Подсчитать сумму цифр в вещественном числе.
#готово

# def counter(num: float):
#     while num != int(num):
#         num *= 10
#     summa = 0
#     while num > 0:
#         summa += num % 10
#         num //= 10
#     return int(summa)

# print(counter(123.321))


# Задача 5. Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
#готово

def factorial(n:int):
    factorial_list = []
    output_list = 1
    for i in range(1, n + 1):
        output_list *= i
        factorial_list.append(output_list)
    return factorial_list

print(factorial(5))