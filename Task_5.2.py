from functools import reduce

"""

2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

a = 'A2'
b = 'C4F'

a, b = list(a), list(b)
print(a)
print(b)

list_1 = [int(''.join(i), 16) for i in [a, b]]
summ = sum(list_1)
mult = reduce(lambda x, y:  x * y, list_1)

i_sum = list(hex(summ).upper()[2:])
i_mult = list(hex(mult).upper()[2:])

print(i_sum)
print(i_mult)
