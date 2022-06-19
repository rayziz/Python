# Программа принимает на вход два числа и проверяет является ли одно квадратом второго

first_value = int(input('Первое число = '))
second_value = int(input('Второе число = '))
if first_value == second_value * second_value:
    print('Первое число является квадратом второго')
elif second_value == first_value * first_value:
    print("Второе число является квадратом первого")
else:
    print('Никто никому не квадрат, ясно?')