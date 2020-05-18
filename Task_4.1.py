import timeit
from random import randint

"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""


z = [8, 3, 15, 6, 4, 2]
a = []


def sort_2(y):
    # линейная сложность (перебираем список)
    for li in y:
        if li % 2 == 0:
            a.append(y.index(li))


sort_2(z)
print(f'Исходный массив - {z}, результат - {a}')
print(timeit.timeit("sort_2(z)", setup="from __main__ import sort_2, z", number=1000))



z = [8, 3, 15, 6, 4, 2]

a = []


def sort_2(y):
    # квадратичная сложность (сначала перебираем список, потом перебираем упорядоченный список)
    y = [i for i in y if i % 2 == 0]
    for j in y:
        a.append(y.index(j))


sort_2(z)
print(f'Исходный массив - {z}, результат - {a}')
print(timeit.timeit("sort_2(z)", setup="from __main__ import sort_2, z", number=1000))

# функция с линейной сложностью работает быстрее, чем функция с квадратичной сложностью.
# В данном случае не намного


