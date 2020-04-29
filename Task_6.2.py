# Рекурсия
import random


def play_2(y):
    try:
        y_2 = int(input(f'Введите число от 0 до 100: '))
    except ValueError: print('Вы ввели не число! ')
    if y == 9:
        return print(f'Попытки закончились! Загаданное число - {x}')
    if x == y_2:
        print(f'Вы угадали! Загаданное число - {x}')
        return print('Молодец!')
    if x != y_2:
        print('Вы не угадали!')
        if y_2 > x:
            print(f'Число {y_2} больше загаданного числа! Еще одна попытка!')
        else:
            print(f'Число {y_2} меньше загаданного числа! Еще одна попытка!')
        y += 1
        play_2(y)


x = random.randint(0, 100)



play_2(0)