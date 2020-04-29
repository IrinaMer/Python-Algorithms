"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных
"""

x = int(input('введите число: '))

numbers = []
num_1 = x // 10000
numbers.append(num_1)
num_2 = x // 1000 % 10
numbers.append(num_2)
num_3 = x // 100 % 10
numbers.append(num_3)
num_4 = x // 10 % 10
numbers.append(num_4)
num_5 = x // 1 % 10
numbers.append(num_5)
print(numbers)

even = 0
odd = 0
for i in numbers:
    if i != 0 and i % 2 == 0:
        even += 1
    if i != 0 and i % 2 != 0:
        odd += 1

print("even:", even)
print("odd:", odd)

