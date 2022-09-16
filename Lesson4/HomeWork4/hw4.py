# Для тех, кто только сейчас видит этот файл, вместо 1 задачи:
# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя
# Готово

# lst = [1, 5, 2, 3, 4, 6, 1, 7]

# def sequence_computing(lst, index = 0, continuing_element = 0):
#     sequence = []
#     previous_count_element = index
#     sequence.append(lst[previous_count_element])
#     for i in range(previous_count_element + continuing_element, len(lst)):
#         if lst[i] > lst[previous_count_element]:
#             previous_count_element = i
#             sequence.append(lst[i])
#     return sequence

# print(sequence_computing(lst))

# def max_sequence_computing(lst):
#     max_sequence = []
#     for i in range(0, len(lst)):
#         for j in range(1, len(lst)):
#             sequence = sequence_computing(lst, index = i, continuing_element = j)
#             length = len(sequence)
#             if length > len(max_sequence):
#                 max_sequence = sequence
#     return max_sequence

# print(max_sequence_computing(lst))


# 2) Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию
# Готово 

# import random
# from random import randint


# with open("hw4.txt", mode="w") as data:
#     length = 10
#     for i in range(length):
#         data.write(f'{random.randint(1, 100)}\n')

# def data_read(filename):
#     with open(filename, mode="r") as filename:
#         data = filename.read().split('\n')
#     data.pop()
#     return list(map(int, data))


# def sorting(data):
#     data = sorted(data)
#     return data

# print(sorting(data_read("hw4.txt")))


# 3) Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0. 
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования). 


def data_read(filename):
    with open(filename, mode="r") as filename:
        data = filename.read().split('\n')
    data.pop()
    return list(map(int, data))



def triplets(nums, target = 0):
	nums.sort()
	n = len(nums)
	for i in range(n - 2):
		k = target - nums[i]
		(low, high) = (i + 1, n - 1)

		while low < high:
			if nums[low] + nums[high] < k:
				low = low + 1

			elif nums[low] + nums[high] > k:
				high = high - 1

			else:
				print((nums[i], nums[low], nums[high]))

				low = low + 1
				high = high - 1


print(triplets(data_read("1Kints.txt")))




