#Камень ножницы бумага

from random import randint 

game = True
answer = ['Камень', 'Ножницы', 'Бумага']

while game:
    player = int(input('Ваш ход'))
    computer = randint(1, 3)
    print (f'Игрок {answer[player - 1]} - Компьютер {answer[computer - 1]} ')

    if player == computer:
        print('Ничья')

    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print('Игрок выиграл')

    else:
        print('Компьютер выиграл')

    print()

    game = int(input('Хотите продолжить? (0 - нет, 1 - да)'))
    


