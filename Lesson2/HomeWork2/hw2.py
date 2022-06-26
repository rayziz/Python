# 1) Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4
# готово

# lst = [1, 2, 3, 4]


# def summa(list):
#     summ = 0
#     for i in range(len(list)):
#         if list[i] % 2 != 0:
#             summ += list[i]
#     return summ

# print(summa(lst))




# 2) Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
# готово

# def transformation(list)


# import math

# lst = [2, 3, 4, 5, 6]


# def transform(list):
#     trans_lst = []
#     for i in range(math.ceil(len(lst) / 2)):
#         trans_lst.append(list[i] * (list[- i - 1]))
#     return trans_lst


# print(transform(lst))



# 3) В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# готово

# lst = [1.1, 1.2, 3.1, 5, 10.01]

# def float_find(list):
#     float_list = []
#     find = 0
#     for i in range(len(list)):
#         float_list.append(list[i] - int(list[i]))
#     find = max(float_list) - min(float_list)
#     return find

# print(float_find(lst))



# 4) Написать программу преобразования десятичного числа в двоичное
# готово

# from turtle import right


# def to_decimals(n:int):
#     decimal_list = []
#     while n > 0:
#         decimal_list.append(n % 2)
#         n = int(n / 2)
#     right_decimal_list = list.reverse(decimal_list)
#     return decimal_list



# print(to_decimals(29))
        
