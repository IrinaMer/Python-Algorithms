from random import randint
"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""

#numbers = []
#for i in range(10):
    #numbers.append(randint(-50, 90))

numbers = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]


def sort_3(num):
    print(num)
    x = max(numbers)
    print(x)
    z = numbers.index(x)
    print(z)
    y = min(numbers)
    print(y)
    li = numbers.index(y)
    print(li)
    num_1 = numbers[:z]
    print(num_1)
    num_2 = numbers[z + 1:]
    print(num_2)
    numbers_2 = num_1 + num_2
    print(numbers_2)
    k = numbers_2.index(y)
    print(k)
    num_3 = numbers_2[:k]
    print(num_3)
    num_4 = numbers_2[k + 1:]
    print(num_4)
    numbers_3 = num_3 + num_4
    print(numbers_3)
    numbers_3.insert(z, y)
    print(numbers_3)
    numbers_3.insert(li, x)
    print(numbers_3)


sort_3(numbers)







