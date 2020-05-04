from random import randint
"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
numbers = []
for i in range(100):
    numbers.append(randint(1, 20))


def sort_4(num):
    numbers = sorted(num)
    for i in numbers:
        x = numbers.count(i)
        y = max(numbers, key=numbers.count)
    print(f'Число, встречающееся в списке максимальное колличество раз - {y}')


sort_4(numbers)
