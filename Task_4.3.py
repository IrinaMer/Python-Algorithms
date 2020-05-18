from random import randint
import timeit

# квадратичная сложность
numbers = []
for i in range(100):
    numbers.append(randint(1, 20))


def sort_4(num):
        numbers = sorted(num)
        for i in numbers:
            x = numbers.count(i)
            y = max(numbers, key=numbers.count)
        return y


sort_4(numbers)
print(f'Число, встречающееся в списке максимальное колличество раз - {sort_4(numbers)}')
print(timeit.timeit("sort_4(numbers)", setup="from __main__ import sort_4, numbers", number=1000))


numbers = []

def sort_4(num):
    # квадратичная сложность
    num = [randint(1, 20) for i in range(100)]
    sorted(num)
    for i in num:
        y = max(num, key=num.count)
        return y


sort_4(numbers)

print(f'Число, встречающееся в списке максимальное колличество раз - {sort_4(numbers)}')
print(timeit.timeit("sort_4(numbers)", setup="from __main__ import sort_4, numbers", number=1000))

# код с квадратичной сложностью имеющий один из двух циклов за пределами функции, работает очень медленно
# для оптимизации кода, цикл был преобразован в генератор и размещен внутри функции. Код стал работать намного
# быстрее