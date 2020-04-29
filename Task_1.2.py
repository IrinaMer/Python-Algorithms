# Ркурсия


def recursion(i):
    if i == '0':
        return print('Ошибка!')
    if i != '*' and i != '-' and i != '+' and i != '/':
        print('Неверно введена арифметическая операция!')
        return recursion(input('Введите знак: '))
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    if i == '*':
        result = num_1 * num_2
        print(f'{num_1} {i} {num_2} = {result}')
    if i == '+':
        result = num_1 + num_2
        print(f'{num_1} {i} {num_2} = {result}')
    if i == '/':
        result = num_1 / num_2
        print(f'{num_1} {i} {num_2} = {result}')
    if i == '-':
        result = num_1 - num_2
        print(f'{num_1} {i} {num_2} = {result}')
    if i != 0:
        recursion(input('Введите знак: '))


recursion(input('Введите знак операции: '))
