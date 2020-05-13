import random

m = random.randint(1, 10)
SIZE = 2 * m + 1
print(f'Длина списка -  {SIZE}')

rand_list = [random.randint(1, 100) for i in range(SIZE)]
print(f'Исходный список {rand_list}')

k = len(rand_list)//2

for i in rand_list:
    x = rand_list[:k]
    y = rand_list[k:]
y_1 = len(y)
x_1 = len(x)
print(f'Левая часть списка  {x}')
print(f'Правая часть {y}')

if x_1 < y_1:
    j = y[0]
    print(f'Медианой является число {j}')
else:
    l = x[-1]
    print(f'Медианой является число {l}')











