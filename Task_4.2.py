import timeit


numbers = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]


def sort_3(num):
    #сложность линейная
    x = max(num)
    z = num.index(x)
    y = min(num)
    li = num.index(y)
    num_1 = num[:z]
    num_2 = num[z + 1:]
    numbers_2 = num_1 + num_2
    k = numbers_2.index(y)
    num_3 = numbers_2[:k]
    num_4 = numbers_2[k + 1:]
    numbers_3 = num_3 + num_4
    numbers_3.insert(z, y)
    numbers_3.insert(li, x)
    return numbers_3


sort_3(numbers)
print(sort_3(numbers))
print(timeit.timeit("sort_3(numbers)", setup="from __main__ import sort_3, numbers", number=1000))



numbers = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]


def sort_3(num):
    #сложность линейная
    x = num[:num.index(max(num))] + num[num.index(max(num)) + 1:]
    y = x[:x.index(min(num))] + x[x.index(min(num)) + 1:]
    y.insert(num.index(max(num)), min(num))
    y.insert(num.index(min(num)), max(num))
    return y


sort_3(numbers)
print(sort_3(numbers))
print(timeit.timeit("sort_3(numbers)", setup="from __main__ import sort_3, numbers", number=1000))

# Обе функции с линейной сложностью. Большое колличество переменных было убрано из кода, но это не
# помоглю и код стал работать даже немного дольше, много времени уходит на обработку не самой переменной
# а ее формулы. Это не эффективно. 
























