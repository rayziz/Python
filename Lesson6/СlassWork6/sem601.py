# 1) Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# а) Добавьте игру против бота
# б)Подумайте как наделить бота "интеллектом"

# S конфет
# За один ход иг-рок может съесть не более половины от всех оставшихся конфет, но не менее одной конфеты.
# Победителем считается игрок, который съел последнюю конфету.

# при K конфет 
# и возможности забирать m конфет 
# формула для победы будет выглядеть: остаток деления K на m+1

# напр 
# k = 2021
# m = 20

# ост = 2021 % 21
from random import randint 

# 1) Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека 
# готово


# print("Добрый день. \n\nПравила игры: В случайном порядке определяется сколько всего конфет и сколько конфет можно брать за ход\n\nПобеждает тот кто забрал последнюю конфету\n")

# start_amount_of_candes = randint(101, 301)

# max_take_per_turn = randint(11, 21)


# def nim(amount_of_candes:int):
#     while amount_of_candes > 0:
#         win_strategy = amount_of_candes % (max_take_per_turn + 1)
#         print(f'Сколько осталось конфет {amount_of_candes}, Напоминаю, что взять можно не более {max_take_per_turn}, Чтобы выиграт бери {win_strategy} конфеет')
#         player1 = int(input('Ход первого игрока'))
#         if player1 < 1 or player1 > max_take_per_turn:
#             while player1 < 1 or player1 > max_take_per_turn:
#                 print(f"Укажите корретное количество, оно должно не более {max_take_per_turn}")
#                 player1 = int(input('Ход первого игрока'))
#         amount_of_candes -= player1
#         if amount_of_candes < 1:
#             print("Первый игрок победил") 
#             break
#         print(f' Сколько осталось конфет {amount_of_candes}, Напоминаю, что взять можно не более {max_take_per_turn}')
#         player2 = int(input('Ход второго игрока'))
#         if player2 < 1 or player2 > max_take_per_turn:
#             while player2 < 1 or player2 > max_take_per_turn:
#                 print(f"Укажите корретное количество, оно должно не более {max_take_per_turn}")
#                 player2 = int(input('Ход второго игрока'))
#         amount_of_candes -= player2
#         if amount_of_candes < 1:
#             print("Второй игрок победил")
#             break
#         else:
#             print("Следующий ход господа\n")


# nim(start_amount_of_candes)

# 1а) Добавьте игру против бота

# print("Добрый день. \n\nПравила игры: В случайном порядке определяется сколько всего конфет и сколько конфет можно брать за ход\n\nПобеждает тот кто забрал последнюю конфету\n")

# start_amount_of_candes = randint(101, 301)

# max_take_per_turn = randint(11, 21)


# def nim(amount_of_candes:int):
#     while amount_of_candes > 0:
#         win_strategy = amount_of_candes % (max_take_per_turn + 1)
#         print(f'Сколько осталось конфет {amount_of_candes}, Напоминаю, что взять можно не более {max_take_per_turn}, Чтобы выиграт бери {win_strategy} конфеет')
#         player1 = int(input('Ход первого игрока'))
#         if player1 < 1 or player1 > max_take_per_turn:
#             while player1 < 1 or player1 > max_take_per_turn:
#                 print(f"Укажите корретное количество, оно должно не более {max_take_per_turn}")
#                 player1 = int(input('Ход первого игрока'))
#         amount_of_candes -= player1
#         if amount_of_candes < 1:
#             print("Первый игрок победил") 
#             break
#         print(f' Сколько осталось конфет {amount_of_candes}, Напоминаю, что взять можно не более {max_take_per_turn}')
#         player2 = randint(1, max_take_per_turn )
#         print(f' Компьютер взял {player2} кофет')
#         amount_of_candes -= player2
#         if amount_of_candes < 1:
#             print("Второй игрок победил")
#             break
#         else:
#             print("Следующий ход господа\n")


# nim(start_amount_of_candes)

# 1б)Подумайте как наделить бота "интеллектом"

print("Добрый день. \n\nПравила игры: В случайном порядке определяется сколько всего конфет и сколько конфет можно брать за ход\n\nПобеждает тот кто забрал последнюю конфету\n")

start_amount_of_candes = randint(101, 301)

max_take_per_turn = randint(11, 21)


def nim(amount_of_candes:int):
    while amount_of_candes > 0:
        win_strategy = amount_of_candes % (max_take_per_turn + 1)
        print(f'Сколько осталось конфет {amount_of_candes}, Напоминаю, что взять можно не более {max_take_per_turn}, Чтобы выиграт бери {win_strategy} конфеет')
        player1 = int(input('Ход первого игрока'))
        if player1 < 1 or player1 > max_take_per_turn:
            while player1 < 1 or player1 > max_take_per_turn:
                print(f"Укажите корретное количество, оно должно не более {max_take_per_turn}")
                player1 = int(input('Ход первого игрока'))
        amount_of_candes -= player1
        if amount_of_candes < 1:
            print("Первый игрок победил") 
            break
        print(f' Сколько осталось конфет {amount_of_candes}, Напоминаю, что взять можно не более {max_take_per_turn}')
        player2 = win_strategy
        print(f' Компьютер взял {player2} кофет')
        amount_of_candes -= player2
        if amount_of_candes < 1:
            print("Второй игрок победил")
            break
        else:
            print("Следующий ход господа\n")


nim(start_amount_of_candes)