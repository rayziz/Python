# Задача с семинара:
# Готово
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random
from random import randint



def create_random_list(k:int):
    return [randint(0, 100) for i in range (k + 1)]

def insert_string_in_file(k, coef_list):
    result_string = ''
    flaf_empty_operator = True
    for i in range (k, -1, -1):
        coef_index = k - i
        coef = coef_list[coef_index]

        if coef == 0:
            continue

        if (flaf_empty_operator):
            separator = ""
            flaf_empty_operator = False

        else:
            separator = " + "

        member = str(coef) + "*x^" + str(i) \
            if coef_index != len(coef_list) - 1 \
            else str(coef)

        result_string += separator + member
    
    result_string += " = 0"
    return result_string

k = 2 

coef_list = create_random_list(k)
print(coef_list)
print(insert_string_in_file(k, coef_list))

with open ('s4', 'w') as data:
    data.write(insert_string_in_file(k, coef_list))

