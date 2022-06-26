# 1) файлы (режимы работы)
# a – добавление данных
# r – чтение
# w – стирание прошлого и запись нового
# также есть такие режимы как w+ и  т.д.

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()


# # 2) В питоне можно умножать строки на числа = строка будет повторена n раз 

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!

# # 3) Если надо несколько параметров для функции, а сколько мы не знаем, то надо поставить звёздочку (строка 22)
# # а уже при вызове функции напишем, сколько надо

# def concatenatio(*params):
# # Тело функции

# print(concatenatio('a', 's', 'd', 'w')) # asdw


# 4) рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 11):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# 5) Кортеж = неизменяемый список. обозначается ()

t1 = (1,)
print(type(t1)) # tuple, для кортежа нужна запятая
t2 = (1)
print(type(t2)) # int
t3 = (1, 3, 5, 6)

for e in t3: # тут достаточно указать е, типо элементс и будет работать
    print(e)


# 6) Неупорядоченные коллекции произвольных
# объектов с доступом по ключу, задаётся dictionary = {}

dictionary = {} # так задаём, что сейчас будет словарь
dictionary = \
{
'up': '↑',
'left': '←',
'down': '↓',
'right': '→'
}

# а через слеш прописываем ключи и не ключи

print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←

del dictionary['left'] # удаление элемента

for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))


# 7) Неупорядоченная совокупность элементов

# !!!
# Большое отличие от list в том, что все элементы уникальны и не может быть повторов,
# поэтому очень удобно использовать для удаления дубликатов
# !!!

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green',

colors.add('gray') #Добавляем элемент в множество, 
#если он уже есть, то ничего не произойдёт
print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
.union(b) \
.difference(a.intersection(b))
# {1, 21, 3, 13}

# 8) чтобы print был в одну строчку можно прописать условие end = ' '

lst = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(lst)):
    print(lst[i]) # вывод в столбец

lst = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(lst)):
    print(lst[i], end = ' ') # вывод в сточку


9) перевенуть список можно с помощью среза списка

lst = [1.1, 1.2, 3.1, 5, 10.01]

print(lst)  # прямой порядок
print(lst[::-1]) # обратный порядок

