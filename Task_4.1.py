"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
"""
#Цикл

def rem(x):
    y = 1
    i = 0
    summ = 0
    while i < x:
        summ += y
        y = y / 2 * -1
        i += 1
        return summ


try:
    x = int(input('Введите колличество элементов: '))
    print(f'Сумма чисел - {rem(x)}, колличество чисел - {x} ')
except ValueError: print('Ошибка!')


