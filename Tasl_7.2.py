import random
import timeit


rand_list = [random.randint(0, 50) for i in range(0, 10)]


def merge_sort(A):

    if len(A) <= 1:
        return A

    l_x = merge_sort(A[:len(A) // 2])
    r_x = merge_sort(A[len(A) // 2:])

    i = j = 0
    result_of_sort = []

    while i < len(l_x) or j < len(r_x):

        if i >= len(l_x):
            result_of_sort.append(r_x[j])
            j += 1

        elif j >= len(r_x):
            result_of_sort.append(l_x[i])
            i += 1

        elif l_x[i] < r_x[j]:
            result_of_sort.append(l_x[i])
            i += 1

        else:
            result_of_sort.append(r_x[j])
            j += 1

    return result_of_sort


print(f'Исходный массив:\n{rand_list}\n')
print(f'Сортированный массив:\n{merge_sort(rand_list)}')

#10
print(timeit.timeit("merge_sort(rand_list)", \
    setup="from __main__ import merge_sort, rand_list", number=1000))

rand_list = [random.randint(0, 50) for i in range(0, 100)]

#100
print(timeit.timeit("merge_sort(rand_list)", \
    setup="from __main__ import merge_sort, rand_list", number=1000))

rand_list = [random.randint(0, 50) for i in range(0, 1000)]

#1000
print(timeit.timeit("merge_sort(rand_list)", \
    setup="from __main__ import merge_sort, rand_list", number=1000))

"""
Результаты кода:

Исходный массив:
[7, 23, 19, 8, 2, 9, 7, 35, 20, 32]

Сортированный массив:
[2, 7, 7, 8, 9, 19, 20, 23, 32, 35]

0.028558215999999997
0.443821744
7.051852658
"""