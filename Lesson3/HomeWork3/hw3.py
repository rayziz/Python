# 1) Найти НОК двух чисел
# готово

# def NOK_finding(m, n):
#     nok = 1
#     while True:
#         if nok % m == 0 and nok % n == 0:
#             break
#         nok += 1
#     return(nok)
    

# print(NOK_finding(16, 20))


# 2) Вычислить число Пи c заданной точностью d
# Пример: при d = 0.0001,  c= 3.1415. 
# готово

# import math

# def calc_pi(epsilon):
#     n = 2
#     pi = 4*[1, -1/3]
#     dif = 1
#     while dif > epsilon:
#         pi.append(4*(-1)**n/ (2 * n + 1))
#         dif = abs(sum(pi[:-1]) - sum(pi[:-2]))
#         n += 1 

#     return math.floor(sum(pi)*int(1/epsilon))*epsilon


# print(calc_pi(0.0001)) 



# 3) Составить список простых множителей натурального числа N
# Готово


# def decompose(n):
#     simple_multiplier_list = []
#     divider = 2
#     while divider <= n:
#         while n % divider == 0:
#             simple_multiplier_list.append(divider)
#             n //= divider
#         divider +=1
#     return simple_multiplier_list 

# print(decompose(45))



# 4) Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# lst = [1, 2, 3, 5, 1, 5, 3, 10]
# new_lst = []

# for i in range(len(lst)):
#     if lst[i] not in new_lst:
#         new_lst.append(lst[i])

# print(new_lst)


# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.
# Готово

# import random
# from random import randint

# count = 10 
# new_lst = []


# with open ('hw3', 'w') as data:
#     for i in range (count):
#         data.writelines(str(randint(0, 9)) + '\n')

# with open ('hw3', 'r') as data:
#     for i in data:
#         if int(i) % 2 != 0:
#             new_lst.append(int(i))

# print(new_lst)

# check = input("Посмотретие файл, потом введите любое число, и проверьте ещё раз. Из файла будут удалены все чётные числа")

# with open ('hw3', 'w') as data:
#         for i in range(len(new_lst)):
#             data.writelines(str(new_lst[i]) + '\n')

# print("Можно смотреть")